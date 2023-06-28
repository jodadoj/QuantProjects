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
    company_name = models.CharField(max_length=300)
    currency = models.CharField(max_length=5)
    exchange = models.CharField(max_length=10)
    mic_code = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    security_type = models.CharField(max_length=50)
    sp500 = models.BooleanField()
    ftse_100 = models.BooleanField()
    nasdaq_100 = models.BooleanField()
    last_updated = models.DateField(default='1901-01-01')

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
    currency_group = models.CharField(max_length=20)
    currency_base = models.CharField(max_length=30)
    currency_quote = models.CharField(max_length=50)

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
    available_exchanges = models.CharField(max_length=100)
    currency_base = models.CharField(max_length=50)
    currency_quote = models.CharField(max_length=50)