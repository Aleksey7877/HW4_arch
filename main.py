import logging
from converters import CurrencyConverter, UsdCnyConverter, UsdRubConverter, UsdEurConverter, UsdGbpConverter

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

    try:
        amount = float(input('Введите сумму в USD: '))
        rates = CurrencyConverter.get_exchange_rates()
        
        rub_converter = UsdRubConverter(rates)
        eur_converter = UsdEurConverter(rates)
        gbp_converter = UsdGbpConverter(rates)
        cny_converter = UsdCnyConverter(rates)

        print(f"{amount} USD = {rub_converter.convert(amount)}")
        print(f"{amount} USD = {eur_converter.convert(amount)}")
        print(f"{amount} USD = {gbp_converter.convert(amount)}")
        print(f"{amount} USD = {cny_converter.convert(amount)}")

    except ValueError:
        logging.error("Неверная сумма")
    except Exception as e:
        logging.error(f"Ошибка: {e}")

if __name__ == "__main__":
    main()