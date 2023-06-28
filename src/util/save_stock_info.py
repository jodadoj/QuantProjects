"""
    Returns all information about a group of stocks e.g. FTSE 100

    Functions
    ---------
    save_all_stock_info_json(string) -> void

    Notes
    -----
    TODAYS_DATE = the date to be recorded on the file system
"""

import glob
import os
import datetime as dt
import pandas as pd
from save_single_stock_info import save_single_stock_info

# import requests_cache
# import yfinance as yf

# session = requests_cache.CachedSession("yfinance.cache")
# session.headers[
#     "User-agent"
# ] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# INCORRECTLY_FORMATED_INDEX = "Unnamed: 0"

TODAYS_DATE = dt.datetime.today().strftime("%Y-%m-%d")


def save_all_stock_info_json(input_path):
    """
    Downloads all stock infomation of given input file list through Yahoo Finance
    
    Arguments
    ----------
    input_path: str
        Path to the csv file that is read to produce the stocks that should be listed
    
    Notes
    -----
    Saves as JSON
    """
    stocks = pd.read_csv(input_path)

    for symbol in stocks["Ticker"]:
        save_single_stock_info(symbol)


# phasing out
# def save_all_stock_info_csv(input_path):
# """
# Downloads all stock infomation of given input file list through Yahoo Finance
#
# Arguments
# ----------
# input_path: str
#     Path to the csv file that is read to produce the stocks that should be listed
#
# Notes
# -----
# Saves as CSV
# """
#     stocks = pd.read_csv(input_path)
#     if INCORRECTLY_FORMATED_INDEX in stocks.keys():
#         stocks = stocks.drop(INCORRECTLY_FORMATED_INDEX, axis=1)

#     for symbol in stocks["Ticker"]:
#         currentStock = yf.Ticker(f"{symbol}", session=session)
#         currentStockData = pd.DataFrame(
#             [list(currentStock.info.values())], columns=list(currentStock.info.keys())
#         )

#         save_path = os.path.join(
#             os.path.realpath(__file__),
#             f"../src/output/individual_stock_data/{TODAYS_DATE}/{TODAYS_DATE}-{symbol}-data.csv",
#         )

#         currentStockData.to_csv(save_path)


if __name__ == "__main__":
    latest_file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        f"../output/sp500_lists/{TODAYS_DATE}-sp500.csv",
    )
    if not os.path.isfile(latest_file_path):
        list_of_files = glob.glob(
            os.path.join(os.path.realpath(os.path.dirname(latest_file_path)), "*.csv")
        )
        latest_file = max(list_of_files, key=os.path.getctime)
        
    save_all_stock_info_json(latest_file_path)
