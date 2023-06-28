"""
    Single file to scrape all wikipedia lists

    Functions
    ---------
    scrape_index_data() -> void/file(s)

    Notes
    -----
"""
from util.scrape_nasdaq_100_wiki import scrape_nasdaq100_wiki
from util.scrape_sp500_wiki import scrape_sp500_wiki
from util.scrape_ftse_100_wiki import scrape_ftse_100_wiki


def scrape_index_data():
    """
    Scrapes wikipedia for current S&P 500, NASDAQ 100 and FTSE 100 lists
    """
    scrape_sp500_wiki()
    scrape_nasdaq100_wiki()
    scrape_ftse_100_wiki()


if __name__ == "__main__":
    scrape_index_data()
