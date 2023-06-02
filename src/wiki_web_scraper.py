import datetime as dt
import pandas as pd

def scrape_sp500_wiki_list():
    """Fetches the current list of S&P500 companies from wikipedia and stores them as a csv file"""
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    data = pd.read_html(url)

    sp500 = data[0].iloc[:, [0,1,5,6]]
    sp500.columns = ['Ticker', 'Name', 'Date', 'CIK']

    mask = sp500['Date'].str.strip().str.fullmatch('\d{4}-\d{2}-\d{2}')
    mask.loc[mask.isnull()] = False
    mask = mask == False

    current = sp500.copy()
    current.loc[mask, 'Date'] = '1900-01-01'
    current.loc[:, 'Date'] = pd.to_datetime(current['Date'])
    current.loc[:, 'CIK'] = current['CIK'].apply(str).str.zfill(10)

    adjustments = data[1]

    columns = ['Date', 'Ticker_Added', 'Name_Added', 'Ticker_Removed', 'Name_Removed', 'Reason']
    adjustments.columns = columns

    additions = adjustments[~adjustments['Ticker_Added'].isnull()][['Date', 'Ticker_Added', 'Name_Added']]
    additions.columns = ['Date','Ticker','Name']
    additions['Action'] = 'Added'

    removals = adjustments[~adjustments['Ticker_Removed'].isnull()][['Date', 'Ticker_Removed', 'Name_Removed']]
    removals.columns = ['Date','Ticker','Name']
    removals['Action'] = 'Removed'

    historical = pd.concat([additions, removals])

    missing = current[~current['Ticker'].isin(historical['Ticker'])].copy()

    missing['Action'] = 'Added'
    missing = missing[['Date', 'Ticker', 'Name', 'Action', 'CIK']]

    sp500_history = pd.concat([historical, missing])
    sp500_history =sp500_history.sort_values(by=['Date', 'Ticker'], ascending=[False, True])

    today = dt.datetime.today().strftime('%Y-%m-%d')

    current.to_csv(f'{today}-sp500.csv')
    sp500_history.to_csv(f'{today}-sp500_history.csv')

def scrape_nasdaq100_wiki_list():
    """Fetches the current list of Nasdaq100 companies from wikipedia and stores them as a csv file"""
    nasdaq_url = 'https://en.wikipedia.org/w/index.php?title=Nasdaq-100'
    nasdaq_data = pd.read_html(nasdaq_url)

    nasdaq100 = nasdaq_data[4].iloc[:, [0,1]]
    nasdaq100.columns = ['Name', 'Ticker']
        
    today = dt.datetime.today().strftime('%Y-%m-%d')

    nasdaq100.to_csv(f'{today}-nasdaq100.csv')


if __name__ == "__main__":
    scrape_sp500_wiki_list()
    scrape_nasdaq100_wiki_list()