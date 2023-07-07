from api.viewsets import StocksViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stocks', StocksViewSet, basename='stock')