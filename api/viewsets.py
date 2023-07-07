"""
    Viewsets of the app. 
    Come with create/retrieve/update/destroy style functions.
"""

from rest_framework import viewsets, permissions
from .serializers import StocksSerializer
from .models import Stocks

class StocksViewSet(viewsets.ModelViewSet):
    """Stocks viewset to recieve all basic functionality of stock table api

    Args:
        viewset
    """
    queryset = Stocks.objects.all().order_by('-last_updated')
    serializer_class = StocksSerializer
    permission_classes = [permissions.IsAuthenticated]
