import logging
from converters import CurrencyConverter


class UsdEurConverter(CurrencyConverter):
    def __init__(self, rates):
        self.rates = rates
        self.logger = logging.getLogger(__name__) 
    
    def convert(self, amount):
        self.logger.info(f"USD->EUR: {amount} * {self.rates['EUR']}")
        return amount * self.rates['EUR']