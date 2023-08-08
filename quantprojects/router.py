from rest_framework import routers
from api.viewsets import StocksViewSet, LiveStocksViewSet

router = routers.DefaultRouter()
router.register('stocks', StocksViewSet, basename='stock')
router.register('livestocks', LiveStocksViewSet, basename='livestock')
