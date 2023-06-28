from django.urls import path
from .views import main, StocksView

urlpatterns = [
    path('', main),
    path('stocks', StocksView.as_view())
]
