import os
import datetime as dt
import pandas as pd

TODAYS_DATE = dt.datetime.today().strftime("%Y-%m-%d")
NASDAQ_LIST_INDEX = 4


def scrape_nasdaq100_wiki():
    """Fetches the current list of Nasdaq100 companies from wikipedia and stores them as a csv file"""
    nasdaq_url = "https://en.wikipedia.org/w/index.php?title=Nasdaq-100"
    nasdaq_data = pd.read_html(nasdaq_url)

    nasdaq100 = nasdaq_data[NASDAQ_LIST_INDEX].iloc[:, [0, 1]]
    nasdaq100.columns = ["Name", "Ticker"]

    nasdaq100.to_csv(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            f"../output/nasdaq_lists/{TODAYS_DATE}-nasdaq100.csv",
        ),
        index=False,
    )
