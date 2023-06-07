import datetime as dt
import pandas as pd
import os

TODAYS_DATE = dt.datetime.today().strftime("%Y-%m-%d")


def scrape_sp500_wiki():
    """Fetches the current list of S&P500 companies from wikipedia and stores them as a csv file"""
    sp500_wiki_link = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    extracted_SP500_table_data = pd.read_html(sp500_wiki_link)

    sp500_table = extracted_SP500_table_data[0].iloc[:, [0, 1, 5, 6]]
    sp500_table.columns = ["Ticker", "Name", "Date", "CIK"]

    missing_date_entries = (
        sp500_table["Date"].str.strip().str.fullmatch("\d{4}-\d{2}-\d{2}")
    )
    missing_date_entries.loc[missing_date_entries.isnull()] = False
    missing_date_entries = missing_date_entries == False

    corrected_sp500 = sp500_table.copy()
    corrected_sp500.loc[missing_date_entries, "Date"] = "1900-01-01"
    corrected_sp500.loc[:, "Date"] = pd.to_datetime(corrected_sp500["Date"])
    corrected_sp500.loc[:, "CIK"] = corrected_sp500["CIK"].apply(str).str.zfill(10)

    adjustments = extracted_SP500_table_data[1]

    columns = [
        "Date",
        "Ticker_Added",
        "Name_Added",
        "Ticker_Removed",
        "Name_Removed",
        "Reason",
    ]
    adjustments.columns = columns

    additions = adjustments[~adjustments["Ticker_Added"].isnull()][
        ["Date", "Ticker_Added", "Name_Added"]
    ]
    additions.columns = ["Date", "Ticker", "Name"]
    additions["Action"] = "Added"

    removals = adjustments[~adjustments["Ticker_Removed"].isnull()][
        ["Date", "Ticker_Removed", "Name_Removed"]
    ]
    removals.columns = ["Date", "Ticker", "Name"]
    removals["Action"] = "Removed"

    historical = pd.concat([additions, removals])

    missing = corrected_sp500[
        ~corrected_sp500["Ticker"].isin(historical["Ticker"])
    ].copy()

    missing["Action"] = "Added"
    missing = missing[["Date", "Ticker", "Name", "Action", "CIK"]]

    sp500_history = pd.concat([historical, missing])
    sp500_history = sp500_history.sort_values(
        by=["Date", "Ticker"], ascending=[False, True]
    )

    corrected_sp500.to_csv(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            f"../output/sp500_lists/{TODAYS_DATE}-sp500.csv",
        ),
        index=False,
    )
    sp500_history.to_csv(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            f"../output/sp500_lists/{TODAYS_DATE}-sp500_history.csv",
        ),
        index=False,
    )

    """
    Link this to database via for loop

    for stock in 
        COPY quantprojects(ticker, date_added)
        FROM file_path - f'output/{today}-sp500.csv'
        DELIMITER ',' CSV;
    
    """
