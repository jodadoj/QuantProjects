"""
    Viewsets of the app. 
    Come with create/retrieve/update/destroy style functions.
"""

from rest_framework import viewsets, permissions
from .serializers import StocksSerializer
from .serializers import LiveStocksSerializer
from .models import Stocks
from .models import LiveStocks

class StocksViewSet(viewsets.ModelViewSet):
    """Stocks viewset to recieve all basic functionality of stock table api

    Args:
        viewset
    """
    queryset = Stocks.objects.all().order_by('-last_updated')
    serializer_class = StocksSerializer
    permission_classes = [permissions.IsAuthenticated]

class LiveStocksViewSet(viewsets.ModelViewSet):
    """LiveStocks viewset to recieve all basic functionality of stock table api

    Args:
        viewset
    """
    queryset = LiveStocks.objects.all().order_by('-timestamp')
    serializer_class = LiveStocksSerializer
    permission_classes = [permissions.IsAuthenticated]
