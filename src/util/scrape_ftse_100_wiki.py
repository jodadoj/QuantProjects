import os
import datetime as dt
import pandas as pd

TODAYS_DATE = dt.datetime.today().strftime("%Y-%m-%d")
FTSE_LIST_INDEX = 4


def scrape_ftse_100_wiki():
    """Fetches the current list of FTSE 100 companies from wikipedia and stores them as a csv file"""
    ftse_url = "https://en.wikipedia.org/wiki/FTSE_100_Index"
    ftse_data = pd.read_html(ftse_url)

    ftse100 = ftse_data[FTSE_LIST_INDEX].iloc[:, [0, 1, 2]]
    ftse100.columns = ["Name", "Ticker", "Sector"]

    ftse100.to_csv(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            f"../output/ftse_lists/{TODAYS_DATE}-ftse_100.csv",
        ),
        index=False,
    )
