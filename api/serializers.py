from rest_framework import serializers
from .models import Stocks, Forex, Crypto

class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = (
            'ticker', 
            'company_name',
            'currency',
            'exchange',
            'mic_code',
            'security_type',
            'sp500',
            'ftse_100',
            'nasdaq_100',
            'last_updated'
            )

class ForexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forex
        fields = (
            'symbol',
            'currency_group', 
            'currency_base',
            'currency_quote'
            )


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = (
            'symbol',
            'available_exchanges', 
            'currency_base',
            'currency_quote'
            )
