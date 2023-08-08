"""
    Returns all information about a single stock

    Functions
    ---------
    save_single_stock(string) -> object

    Notes
    -----
    TODAYS_DATE = the date to be recorded on the file system
"""
import os
import json
import datetime as dt
import yahooquery as yq

TODAYS_DATE = dt.datetime.today().strftime("%Y-%m-%d")


def save_single_stock_info(ticker):
    """
    Downloads all inform of a destignated ticker passed to the function through Yahoo Finance
    

    Arguments
    ----------
    ticker: str
        Ticker symbol for the stock to be grabbed
    
    Notes
    -----
    The function also takes a list of strings but this is unwanted behaviour
        
    """
    save_path = os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            f"../output/individual_stock_data/{TODAYS_DATE}/{TODAYS_DATE}-{ticker}-data.json",
        )
    )

    if not os.path.isfile(save_path):
        try:
            os.makedirs(os.path.realpath(os.path.dirname(save_path)))
        except FileExistsError:
            pass

        current_stock = yq.Ticker(ticker, asynchronous=True)
        current_stock_data = current_stock.all_modules

        with open(save_path, "w", encoding="utf-8") as stock_file:
            json.dump(current_stock_data, stock_file, indent=4, sort_keys=False)
