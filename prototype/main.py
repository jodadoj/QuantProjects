import os
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from dotenv import load_dotenv


def load_local_data():
    stocks = pd.read_csv("sp_500_stocks.csv")
    load_dotenv()
    return stocks


def fetch_alpha_vantage_data():
    stocks = load_local_data()
    av_api_key = os.environ.get("ALPHA_VANTAGE_API_TOKEN")

    symbol = "AAPL"
    overview_url = (
        "https://www.alphavantage.co/query?function=OVERVIEW&symbol="
        f"{symbol}&apikey={av_api_key}"
    )
    overview_req = requests.get(overview_url, timeout=10)
    overview_data = overview_req.json()
    market_cap = overview_data["MarketCapitalization"]

    time_series_url = (
        "https://www.alphavantage.co/query?function="
        f"TIME_SERIES_INTRADAY&symbol={symbol}&interval="
        f"5min&apikey={av_api_key}"
    )
    req = requests.get(time_series_url, timeout=10)
    time_series_data = req.json()
    return [overview_data, time_series_data]


def create_dataframes():
    [overview_data, time_series_data] = fetch_alpha_vantage_data()
    market_cap = overview_data["MarketCapitalization"]
    last_refresh = time_series_data["Meta Data"]["3. Last Refreshed"]
    recent_prices = time_series_data["Time Series (5min)"][f"{last_refresh}"]
    open_price = recent_prices["1. open"]
    high_price = recent_prices["2. high"]
    low_price = recent_prices["3. low"]
    close_price = recent_prices["4. close"]
    volume_price = recent_prices["5. volume"]

    headings = [
        "Ticker",
        "Stock Price",
        "Market Capitalisation",
        "Number of Shares to Buy",
    ]
    result = pd.DataFrame(columns=headings)

    result.append(
        pd.Series([symbol, close_price, market_cap, "N/A"], index=headings),
        ignore_index=True,
    )


def chunks(list, n):
    """Yield successive n-sized chunks from list"""
    for i in range(0, len(list), n):
        yield list[i : i + n]
