import  logging
from converters import CurrencyConverter


class UsdGbpConverter(CurrencyConverter):
    def __init__(self, rates):
        self.rates = rates
        self.logger = logging.getLogger(__name__) 
    
    def convert(self, amount):
        self.logger.info(f"USD->GBP: {amount} * {self.rates['GBP']}")
        return amount * self.rates['GBP']