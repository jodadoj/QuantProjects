from django.db import models
import random
import string

# Create your models here.

def generate_random_code(length=8):
    """
    Generates a random code to assign to values where a serial id would be inappropriate
    -------
    Arguments
    -------
    length - the length of the string we will to create
    """
    code = ''.join(random.choices(
        population=(string.digits, string.ascii_letters),
        k=length
                                  ))
    return code

class Stocks(models.Model):
    """
    Table representing the list of stocks known to the database
    -------
    Fields
    -------
    Ticker - The ticker symbol of the company

    Company name - The name of the company

    Currency - The currency it trades in (useful for forex arbitrage)
    
    Exchange - The exchange it is listed on
    
    mic_code - The unique code of the exchange
    
    Country - The country the company exists in
    
    Security type - The type of security being traded (possibly redundant)
    
    S&P500 - Whether it is a member of the S&P500
    
    FTSE 100 - Whether it is a member of the FTSE 100
    
    NASDAQ 100 - Whether it is a member of the NASDAQ 100
 
    Last Updated - The last date these values where checked

    """
    ticker = models.CharField(primary_key=True, max_length=10)
    company_name = models.CharField(max_length=300, null=True)
    currency = models.CharField(max_length=5)
    exchange = models.CharField(max_length=10, null=True)
    mic_code = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=30, null=True)
    security_type = models.CharField(max_length=50, null=True)
    sp500 = models.BooleanField()
    ftse_100 = models.BooleanField()
    nasdaq_100 = models.BooleanField()
    last_updated = models.DateField(default='1901-01-01')
    enterpriseValue = models.FloatField(max_length=30, null=True)
    forwardPE = models.FloatField(max_length=30, null=True)
    profitMargins = models.FloatField(max_length=30, null=True)
    floatShares = models.FloatField(max_length=30, null=True)
    sharesOutstanding = models.FloatField(max_length=30, null=True)
    sharesShort = models.FloatField(max_length=30, null=True)
    sharesShortPriorMonth = models.DateField(default='1901-01-01')
    sharesShortPreviousMonthDate = models.DateField(default='1901-01-01')
    dateShortInterest = models.FloatField(max_length=30, null=True)
    sharesPercentSharesOut = models.FloatField(max_length=30, null=True)
    heldPercentInsiders = models.FloatField(max_length=30, null=True)
    heldPercentInstitutions = models.FloatField(max_length=30, null=True)
    shortRatio = models.FloatField(max_length=30, null=True)
    shortPercentOfFloat = models.FloatField(max_length=30, null=True)
    beta = models.FloatField(max_length=30, null=True)
    impliedSharesOutstanding = models.FloatField(max_length=30, null=True)
    bookValue = models.FloatField(max_length=30, null=True)
    priceToBook = models.FloatField(max_length=30, null=True)
    lastFiscalYearEnd = models.DateField(default='1901-01-01')
    nextFiscalYearEnd = models.DateField(default='1901-01-01')
    mostRecentQuarter = models.DateField(default='1901-01-01')
    earningsQuarterlyGrowth = models.FloatField(max_length=30, null=True)
    netIncomeToCommon = models.FloatField(max_length=30, null=True)
    trailingEps = models.FloatField(max_length=30, null=True)
    forwardEps = models.FloatField(max_length=30, null=True)
    pegRatio = models.FloatField(max_length=30, null=True)
    lastSplitFactor = models.FloatField(max_length=30, null=True)
    lastSplitDate = models.FloatField(max_length=30, null=True)
    enterpriseToRevenue = models.FloatField(max_length=30, null=True)
    enterpriseToEbitda = models.FloatField(max_length=30, null=True)
    fiftyTwoWeekChange = models.FloatField(max_length=30, null=True)
    sandP52WeekChange = models.FloatField(max_length=30, null=True)
    lastDividendValue = models.FloatField(max_length=30, null=True)
    lastDividendDate = models.FloatField(max_length=30, null=True)
    currentPrice = models.FloatField(max_length=30, null=True)
    targetHighPrice = models.FloatField(max_length=30, null=True)
    targetLowPrice = models.FloatField(max_length=30, null=True)
    targetMeanPrice = models.FloatField(max_length=30, null=True)
    targetMedianPrice = models.FloatField(max_length=30, null=True)
    totalCash = models.FloatField(max_length=30, null=True)
    totalCashPerShare = models.FloatField(max_length=30, null=True)
    ebitda = models.FloatField(max_length=30, null=True)
    totalDebt = models.FloatField(max_length=30, null=True)
    quickRatio = models.FloatField(max_length=30, null=True)
    currentRatio = models.FloatField(max_length=30, null=True)
    totalRevenue = models.FloatField(max_length=30, null=True)
    debtToEquity = models.FloatField(max_length=30, null=True)
    revenuePerShare = models.FloatField(max_length=30, null=True)
    returnOnAssets = models.FloatField(max_length=30, null=True)
    returnOnEquity = models.FloatField(max_length=30, null=True)
    grossProfits = models.FloatField(max_length=30, null=True)
    freeCashflow = models.FloatField(max_length=30, null=True)
    operatingCashflow = models.FloatField(max_length=30, null=True)
    earningsGrowth = models.FloatField(max_length=30, null=True)
    revenueGrowth = models.FloatField(max_length=30, null=True)
    grossMargins = models.FloatField(max_length=30, null=True)
    ebitdaMargins = models.FloatField(max_length=30, null=True)
    operatingMargins = models.FloatField(max_length=30, null=True)
    previousClose = models.FloatField(max_length=30, null=True)
    open = models.FloatField(max_length=30, null=True)
    dayLow = models.FloatField(max_length=30, null=True)
    dayHigh = models.FloatField(max_length=30, null=True)
    regularMarketPreviousClose = models.FloatField(max_length=30, null=True)
    regularMarketOpen = models.FloatField(max_length=30, null=True)
    regularMarketDayLow = models.FloatField(max_length=30, null=True)
    regularMarketDayHigh = models.FloatField(max_length=30, null=True)
    dividendRate = models.FloatField(max_length=30, null=True)
    dividendYield = models.FloatField(max_length=30, null=True)
    payoutRatio = models.FloatField(max_length=30, null=True)
    fiveYearAvgDividendYield = models.FloatField(max_length=30, null=True)
    trailingPE = models.FloatField(max_length=30, null=True)
    volume = models.FloatField(max_length=30, null=True)
    regularMarketVolume = models.FloatField(max_length=30, null=True)
    averageVolume = models.FloatField(max_length=30, null=True)
    averageVolume10days = models.FloatField(max_length=30, null=True)
    averageDailyVolume10Day = models.FloatField(max_length=30, null=True)
    bid = models.FloatField(max_length=30, null=True)
    ask = models.FloatField(max_length=30, null=True)
    bidSize = models.FloatField(max_length=30, null=True)
    askSize = models.FloatField(max_length=30, null=True)
    marketCap = models.FloatField(max_length=30, null=True)
    fiftyTwoWeekLow = models.FloatField(max_length=30, null=True)
    fiftyTwoWeekHigh = models.FloatField(max_length=30, null=True)
    priceToSalesTrailing12Months = models.FloatField(max_length=30, null=True)
    fiftyDayAverage = models.FloatField(max_length=30, null=True)
    twoHundredDayAverage = models.FloatField(max_length=30, null=True)
    trailingAnnualDividendRate = models.FloatField(max_length=30, null=True)
    trailingAnnualDividendYield = models.FloatField(max_length=30, null=True)



class Forex(models.Model):
    """
    Table representing the list of forex known to the database
    -------
    Fields
    -------
    Symbol - The  symbol representing the currency
    Currency group - 
    Currency base - 
    Currency quote - 
    """
    symbol = models.CharField(primary_key=True, max_length=10)
    currency_group = models.CharField(max_length=20, null=True)
    currency_base = models.CharField(max_length=30, null=True)
    currency_quote = models.CharField(max_length=50, null=True)
    last_updated = models.DateField(default='1901-01-01')

class Crypto(models.Model):
    
    """
    Table representing the list of cryptocurrencies known to the database
    -------
    Fields
    -------
    Symbol - The  symbol representing the currency
    Availible exchanges - Known exchanges that trade said currency
    Currency base - 
    Currency quote - 
    """
    symbol = models.CharField(primary_key=True, max_length=20)
    available_exchanges = models.CharField(max_length=100, null=True)
    currency_base = models.CharField(max_length=50, null=True)
    currency_quote = models.CharField(max_length=50, null=True)
    last_updated = models.DateField(default='1901-01-01')
    
    