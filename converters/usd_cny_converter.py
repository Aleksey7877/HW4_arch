import logging
from converters import CurrencyConverter

class UsdCnyConverter(CurrencyConverter):
    def __init__(self, rates):
        self.rates = rates
        self.logger = logging.getLogger(__name__) 
    
    def convert(self, amount):
        self.logger.info(f"USD->CNY: {amount} * {self.rates['CNY']}")
        return amount * self.rates['CNY']
    
