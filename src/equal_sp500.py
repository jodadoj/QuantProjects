import os
import numpy as np
import pandas as pd
import requests
import requests_cache
import xlsxwriter 
import math
import yfinance as yf
import datetime as dt
from dotenv import load_dotenv

session = requests_cache.CachedSession('yfinance.cache')
session.headers['User-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'


def fetch_sp500_data():
    """Fetches current financial market data from Yahoo finance public api"""
    file_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)), 'output/2023-06-01-sp500.csv'
            )
    stocks = pd.read_csv(file_path)
    load_dotenv()

    headings = [ 'Ticker', 'Stock Price', 'Market Capitalisation', 'Number of Shares to Buy']
    result = pd.DataFrame(columns=headings)
    symbol_groups = list(chunks(stocks['Ticker'], 101))
    every_str = []
    for i in range(0, len(symbol_groups)):
        every_str.append(','.join(symbol_groups[i]))
    final = pd.DataFrame(columns=headings)
    for symbol_string in every_str:
        for stock in symbol_string.split(','):
            this_stock = yf.Ticker(f"{stock}", session=session)
            try:
                final = final.append(
                    pd.Series(
                    [
                        stock,
                        this_stock.info['currentPrice'],
                        this_stock.info['marketCap'],
                        "N/A"
                    ],
                    index = headings
                    ),
                    ignore_index=True
            )
            except(KeyError):
                pass
    return final

def convert_sp500_data_to_csv():
    """Takes current data from the Yahoo finance metrics and returns as a CSV"""
    final = fetch_sp500_data()
    today = dt.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    file_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)), f'output/{today}-full_sp500_data.csv'
            )
    final.to_csv(file_path)

def chunks(chunk_list, no_of_chunks):
    """Yield successive n-sized chunks from list"""
    for i in range(0, len(chunk_list), no_of_chunks):
        yield chunk_list[i:i + no_of_chunks]

def calculate_no_of_shares_to_purchase():
    """Uses a rudimentary calculation to set the amount needed to purchase equal weights"""
    val = None
    while val == None:
        portfolio_size = input('Enter the value of your portfolio: ')
        try:
            val = float(portfolio_size)
        except(ValueError):
            print('Not a number, please enter a legitamate value:')
        try:
            current_values = pd.read_csv(os.path.join(
                os.path.dirname(os.path.realpath(__file__)), 'output/2023-06-01-15-54-22-full_sp500_data.csv')
            )
        except(FileNotFoundError):
            current_values = pd.read_csv(os.path.join(
                os.path.dirname(os.path.realpath(__file__)), 'output/2023-06-01-15-54-22-full_sp500_data.csv')
            )
            #update above freely
            #eventually iterate through this

    current_values = current_values.drop('Unnamed: 0', axis=1)

    position_size = val/len(current_values.index)
    for i in range(0, len(current_values.index)):
        current_values.loc[i, 'Number of Shares to Buy'] = math.floor(position_size / current_values['Stock Price'][i])
    return current_values

def output_equal_weights_to_excel():
    """Creates an xlxs document to be used with the csv data created"""
    current_values = calculate_no_of_shares_to_purchase()
    today = dt.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    file_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)), f'output/{today}-recommended_trades.xlsx'
            )

    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    current_values.to_excel(writer, sheet_name='Recommended Trades', index = False)

    background_color = '#0a0a23'
    font_color = '#ffffff'

    string_format = writer.book.add_format(
            {
                'font_color': font_color,
                'bg_color': background_color,
                'border': 1
            }
        )

    dollar_format = writer.book.add_format(
            {
                'num_format':'$0.00',
                'font_color': font_color,
                'bg_color': background_color,
                'border': 1
            }
        )

    integer_format = writer.book.add_format(
            {
                'num_format':'0',
                'font_color': font_color,
                'bg_color': background_color,
                'border': 1
            }
        )
    column_formats = { 
                    'A': ['Ticker', string_format],
                    'B': ['Price', dollar_format],
                    'C': ['Market Capitalization', dollar_format],
                    'D': ['Number of Shares to Buy', integer_format]
                    }

    for column in column_formats.keys():
        writer.sheets['Recommended Trades'].set_column(f'{column}:{column}', 20, column_formats[column][1])
        writer.sheets['Recommended Trades'].write(f'{column}1', column_formats[column][0], string_format)

    writer.save()

    
if __name__ == "__main__":
    convert_sp500_data_to_csv()
    output_equal_weights_to_excel()