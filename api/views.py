from rest_framework import generics
from .serializers import StocksSerializer
from .models import Stocks

class StocksView(generics.CreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer


