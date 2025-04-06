import logging
from converters import CurrencyConverter


class UsdRubConverter(CurrencyConverter):
    def __init__(self, rates):
        self.rates = rates
        self.logger = logging.getLogger(__name__) 
    
    def convert(self, amount):
        self.logger.info(f"USD->RUB: {amount} * {self.rates['RUB']}")
        return amount * self.rates['RUB']