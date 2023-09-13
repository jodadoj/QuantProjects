from rest_framework import generics
from .serializers import StocksSerializer, LiveStocksSerializer
from .models import Stocks, LiveStocks

class StocksView(generics.CreateAPIView):
    """Stocks view to recieve all basic functionality of stock table api

    Args:
        generics (_type_): _description_
    """
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer

class LiveStocksView(generics.CreateAPIView):
    """LiveStocks view to recieve all basic functionality of stock table api

    Args:
        generics (_type_): _description_
    """
    queryset = LiveStocks.objects.all()
    serializer_class = LiveStocksSerializer



