from django.db import models

class Currency(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    currency_name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return f'{self.currency_name} ({self.currency_code})'

class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='base_currency_rates')
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='target_currency_rates')
    rate = models.DecimalField(max_digits=15, decimal_places=6)
    date = models.DateField()
    def __str__(self):
        return f'{self.base_currency} -> {self.target_currency} : {self.rate} on {self.date}'


class HistoricalExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='base_currency_history')
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='target_currency_history')
    old_rate = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    new_rate = models.DecimalField(max_digits=15, decimal_places=6)
    change_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Historical Rate {self.base_currency} -> {self.target_currency} : {self.new_rate} on {self.change_date}'
