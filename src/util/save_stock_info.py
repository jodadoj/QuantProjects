import os
import pandas as pd
import requests_cache
import datetime as dt
import yfinance as yf

session = requests_cache.CachedSession("yfinance.cache")
session.headers[
    "User-agent"
] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

INCORRECTLY_FORMATED_INDEX = "Unnamed: 0"
TODAYS_DATE = dt.datetime.today().strftime("%Y-%m-%d")


def save_stock_info(file_path):
    """Downloads all stock infomation of given input file list through Yahoo Finance"""
    stocks = pd.read_csv(file_path)
    if INCORRECTLY_FORMATED_INDEX in stocks.keys():
        stocks = stocks.drop(INCORRECTLY_FORMATED_INDEX, axis=1)

    for symbol in stocks["Ticker"]:
        currentStock = yf.Ticker(f"{symbol}", session=session)
        currentStockData = pd.DataFrame(
            [list(currentStock.info.values())], columns=list(currentStock.info.keys())
        )

        save_path = os.path.join(
            os.path.realpath(__file__),
            f"../src/output/individual_stock_data/{TODAYS_DATE}/{TODAYS_DATE}-{symbol}-data.csv",
        )

        currentStockData.to_csv(save_path)


if __name__ == "__main__":
    try:
        file_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            f"../output/sp500_lists/{TODAYS_DATE}-sp500.csv",
        )
        save_stock_info(file_path)
    except (OSError):
        file_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "../output/sp500_lists/2023-06-06-sp500.csv",
        )
        save_stock_info(file_path)
