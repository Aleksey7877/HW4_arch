from abc import ABC, abstractmethod
import json
import time
import os
import requests
import logging
from typing import Dict, Optional

class CurrencyConverter(ABC):
    _CACHE_FILE = "exchange_rates.json"
    _CACHE_EXPIRY = 3600
    
    @classmethod
    def _load_from_cache(cls) -> Optional[Dict[str, float]]:
        if not os.path.exists(cls._CACHE_FILE):
            return None
        try:
            with open(cls._CACHE_FILE, 'r') as f:
                data = json.load(f)
                if time.time() - data['timestamp'] < cls._CACHE_EXPIRY:
                    return data['rates']
        except (json.JSONDecodeError, KeyError, IOError) as e:
            logging.warning(f"Cache load error: {e}")
            return None

    @classmethod
    def _save_to_cache(cls, rates: Dict[str, float]) -> None:
        try:
            data = {
                'timestamp': time.time(),
                'rates': rates
            }
            with open(cls._CACHE_FILE, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            logging.error(f"Cache save error: {e}")

    @classmethod
    def get_exchange_rates(cls) -> Dict[str, float]:
        """Получение курсов с использованием кеша"""
        rates = cls._load_from_cache()
        if rates:
            logging.info("Using cached rates")
            return rates
            
        try:
            logging.info("Fetching fresh rates from API")
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5)
            response.raise_for_status()
            rates = response.json()['rates']
            cls._save_to_cache(rates)
            return rates
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            raise

    @abstractmethod
    def __init__(self, rates: Dict[str, float]):
        self.rates = rates
    
    @abstractmethod
    def convert(self, amount: float) -> float:
        pass
