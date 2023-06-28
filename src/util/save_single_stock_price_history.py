"""
    Returns full price history for a single stock

    Functions
    ---------
    save_single_stock_price_history(string) -> object

    Notes
    -----
    TODAYS_DATE = the date to be recorded on the file system
"""
import os
import json
import datetime as dt
import yahooquery as yq

TODAYS_DATE = dt.datetime.today().strftime("%Y-%m-%d")


def save_single_stock_price_history(ticker):
    """
    Downloads all prices of a destignated ticker passed to the function through Yahoo Finance
    

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
            f"../output/stock_price_history/{TODAYS_DATE}/{TODAYS_DATE}-{ticker}-prices.csv",
        )
    )

    try:
        os.makedirs(os.path.realpath(os.path.dirname(save_path)))
    except FileExistsError:
        pass

    if not os.path.isfile(save_path):
        current_stock = yq.Ticker(ticker, asynchronous=True)
        current_stock_history = current_stock.history(period='10y', interval='1d')

        current_stock_history.to_csv(save_path, index=False)
