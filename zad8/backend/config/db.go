package config

import (
	_ "github.com/lib/pq"
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
