from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Currency, ExchangeRate, HistoricalExchangeRate

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def currency_list(request):
    currencies = Currency.objects.all()
    return render(request, 'test1.html', {'currencies': currencies})

def exchange_rate_list(request):
    exchange_rates = ExchangeRate.objects.all()
    return render(request, 'test2.html', {'exchange_rates': exchange_rates})

def historical_exchange_rate_list(request):
    historical_rates = HistoricalExchangeRate.objects.all()
    return render(request, 'test2.html', {'historical_rates': historical_rates})
