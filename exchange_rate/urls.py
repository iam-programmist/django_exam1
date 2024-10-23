from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", home, name = "home"),
    path('currencies/', currency_list, name='currency_list'),
    path('exchange-rates/', exchange_rate_list, name='exchange_rate_list'),
    path('historical-rates/', historical_exchange_rate_list, name='historical_exchange_rate_list'),
]