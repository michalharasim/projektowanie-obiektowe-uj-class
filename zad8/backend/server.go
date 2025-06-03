package main

import (
	"net/http"
	"time"

	"github.com/dgrijalva/jwt-go"
	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
	"golang.org/x/crypto/bcrypt"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type User struct {
	ID       uint   `json:"id" gorm:"primaryKey"`
	Username string `json:"username" gorm:"unique"`
	Password string `json:"password"`
}

var db *gorm.DB

func init() {
	var err error
	db, err = gorm.Open(postgres.Open("host=localhost user=postgres dbname=zad8 sslmode=disable"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	db.AutoMigrate(&User{})
}

var secretKey = []byte("mysecretkey")

func main() {
	e := echo.New()

	e.Use(middleware.Logger())
	e.Use(middleware.Recover())
	e.Use(middleware.CORS())

	e.POST("/register", register)
	e.POST("/login", login)

	e.GET("/protected", validateToken(func(c echo.Context) error {
		return c.JSON(http.StatusOK, "Protected data")
	}))

	e.Logger.Fatal(e.Start(":1323"))
}

func hashPassword(password string) (string, error) {
	bytes, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	return string(bytes), err
}

func checkPasswordHash(password, hash string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
	return err == nil
}

func register(c echo.Context) error {
	var request struct {
		Username string `json:"username"`
		Password string `json:"password"`
	}

	if err := c.Bind(&request); err != nil {
		return c.JSON(http.StatusBadRequest, "Invalid JSON input")
	}

	if request.Username == "" || request.Password == "" {
		return c.JSON(http.StatusBadRequest, "Username and password are required")
	}

	var user User
	if err := db.Where("username = ?", request.Username).First(&user).Error; err == nil {
		return c.JSON(http.StatusBadRequest, "Username already taken")
	}

	passwordHash, err := hashPassword(request.Password)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, "Error hashing password")
	}

	user = User{
		Username: request.Username,
		Password: passwordHash,
	}

	if err := db.Create(&user).Error; err != nil {
		return c.JSON(http.StatusInternalServerError, "Error saving user")
	}

	return c.JSON(http.StatusOK, "User created successfully")
}

func login(c echo.Context) error {
	var request struct {
		Username string `json:"username"`
		Password string `json:"password"`
	}

	if err := c.Bind(&request); err != nil {
		return c.JSON(http.StatusBadRequest, "Invalid JSON input")
	}

	var user User
	if err := db.Where("username = ?", request.Username).First(&user).Error; err != nil {
		return c.JSON(http.StatusUnauthorized, "Invalid credentials")
	}

	if !checkPasswordHash(request.Password, user.Password) {
		return c.JSON(http.StatusUnauthorized, "Invalid credentials")
	}

	token := jwt.New(jwt.SigningMethodHS256)
	claims := token.Claims.(jwt.MapClaims)
	claims["username"] = user.Username
	claims["exp"] = time.Now().Add(time.Hour * 24).Unix()

	tokenString, err := token.SignedString(secretKey)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, "Error generating token")
	}

	return c.JSON(http.StatusOK, echo.Map{
		"token": tokenString,
	})
}

func validateToken(next echo.HandlerFunc) echo.HandlerFunc {
	return func(c echo.Context) error {
		authHeader := c.Request().Header.Get("Authorization")
		if authHeader == "" {
			return c.JSON(http.StatusUnauthorized, "Missing token")
		}

		tokenStr := authHeader[len("Bearer "):]
		token, err := jwt.Parse(tokenStr, func(token *jwt.Token) (interface{}, error) {
			return secretKey, nil
		})

		if err != nil || !token.Valid {
			return c.JSON(http.StatusUnauthorized, "Invalid token")
		}

		return next(c)
	}
}
