from django.urls import path
from .views import StocksView
from .viewsets import StocksViewSet

urlpatterns = [
    # path('', StocksViewSet()),
    # path('', StocksView.as_view())
]
