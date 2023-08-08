from rest_framework import serializers
from .models import LiveStocks, Stocks, Forex, Crypto

class LiveStocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStocks
        fields = (
            'id',
            'exchange',
            'quoteType',
            'price',
            'timestamp',
            'marketHours',
            'changePercent',
            'dayVolume',
            'change',
            'priceHint'
        )

#note changed 52WeekChange _> fiftyTwoWeekChange
class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = (
            'ticker', 
            'company_name',
            'currency',
            'exchange',
            'mic_code',
            'country',
            'security_type',
            'sp500',
            'ftse_100',
            'nasdaq_100',
            'last_updated',
            'enterpriseValue',
            'forwardPE',
            'profitMargins',
            'floatShares',
            'sharesOutstanding',
            'sharesShort',
            'sharesShortPriorMonth',
            'sharesShortPreviousMonthDate',
            'dateShortInterest',
            'sharesPercentSharesOut',
            'heldPercentInsiders',
            'heldPercentInstitutions',
            'shortRatio',
            'shortPercentOfFloat',
            'beta',
            'impliedSharesOutstanding',
            'bookValue',
            'priceToBook',
            'lastFiscalYearEnd',
            'nextFiscalYearEnd',
            'mostRecentQuarter',
            'earningsQuarterlyGrowth',
            'netIncomeToCommon',
            'trailingEps',
            'forwardEps',
            'pegRatio',
            'lastSplitFactor',
            'lastSplitDate',
            'enterpriseToRevenue',
            'enterpriseToEbitda',
            'fiftyTwoWeekChange',
            'sandP52WeekChange',
            'lastDividendValue',
            'lastDividendDate',
            'currentPrice',
            'targetHighPrice',
            'targetLowPrice',
            'targetMeanPrice',
            'targetMedianPrice',
            'totalCash',
            'totalCashPerShare',
            'ebitda',
            'totalDebt',
            'quickRatio',
            'currentRatio',
            'totalRevenue',
            'debtToEquity',
            'revenuePerShare',
            'returnOnAssets',
            'returnOnEquity',
            'grossProfits',
            'freeCashflow',
            'operatingCashflow',
            'earningsGrowth',
            'revenueGrowth',
            'grossMargins',
            'ebitdaMargins',
            'operatingMargins',
            'previousClose',
            'open',
            'dayLow',
            'dayHigh',
            'regularMarketPreviousClose',
            'regularMarketOpen',
            'regularMarketDayLow',
            'regularMarketDayHigh',
            'dividendRate',
            'dividendYield',
            'payoutRatio',
            'fiveYearAvgDividendYield',
            'trailingPE',
            'volume',
            'regularMarketVolume',
            'averageVolume',
            'averageVolume10days',
            'averageDailyVolume10Day',
            'bid',
            'ask',
            'bidSize',
            'askSize',
            'marketCap',
            'fiftyTwoWeekLow',
            'fiftyTwoWeekHigh',
            'priceToSalesTrailing12Months',
            'fiftyDayAverage',
            'twoHundredDayAverage',
            'trailingAnnualDividendRate',
            'trailingAnnualDividendYield'
            )

class ForexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forex
        fields = (
            'symbol',
            'currency_group', 
            'currency_base',
            'currency_quote',
            'last_updated'
            )


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = (
            'symbol',
            'available_exchanges', 
            'currency_base',
            'currency_quote',
            'last_updated'
            )
