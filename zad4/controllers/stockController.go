package controllers

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"zad4/models"

	"github.com/labstack/echo/v4"
)

type TimeSeriesResponse struct {
	Values []struct {
		Close    string `json:"close"`
		Datetime string `json:"datetime"`
	} `json:"values"`
}

func GetStock(c echo.Context) error {
	symbol := c.Param("symbol")
	apiKey := "cb0b0c8718be49f5a9df0cffe4803094"
	url := fmt.Sprintf("https://api.twelvedata.com/time_series?symbol=%s&interval=1min&apikey=%s", symbol, apiKey)

	resp, err := http.Get(url)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "failed to fetch data"})
	}
	defer resp.Body.Close()

	body, _ := ioutil.ReadAll(resp.Body)

	var apiResp TimeSeriesResponse
	if err := json.Unmarshal(body, &apiResp); err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "failed to parse API response"})
	}

	if len(apiResp.Values) == 0 {
		return c.JSON(http.StatusNotFound, map[string]string{"error": "no data available"})
	}

	stock := models.Stock{
		Symbol: symbol,
		Price:  apiResp.Values[0].Close,
	}

	return c.JSON(http.StatusOK, stock)
}
