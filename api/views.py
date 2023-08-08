from rest_framework import generics
from .serializers import StocksSerializer, LiveStocksSerializer
from .models import Stocks, LiveStocks

class StocksView(generics.CreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer

class LiveStocksView(generics.CreateAPIView):
    queryset = LiveStocks.objects.all()
    serializer_class = LiveStocksSerializer



