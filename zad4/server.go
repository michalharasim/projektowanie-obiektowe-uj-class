package main

import (
	"zad4/controllers"

	"github.com/labstack/echo/v4"
)

func main() {
	e := echo.New()

	stocks := e.Group("/stocks")
	stocks.GET("/:symbol", controllers.GetStock)

	e.Logger.Fatal(e.Start(":8080"))
}
