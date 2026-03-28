# external_api.py
import requests

# Прямое указание API ключа и URL
API_KEY = "iNJjtsrCm8C6dmn9rsjbd42geeVAWmVD"
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_transaction_to_rub(transaction: dict) -> float:
    """
    Конвертирует транзакцию из валюты transaction['currency'] в рубли.

    :param transaction: словарь {"amount": число, "currency": строка}
    :return: сумма в рублях (float)
    """
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency", "RUB")

    if currency.upper() == "RUB":
        return float(amount)  # если уже в рублях, ничего не делаем

    params = {"from": currency.upper(), "to": "RUB", "amount": amount}
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(BASE_URL, headers=headers, params=params, timeout=5)
        response.raise_for_status()  # выброс исключения при ошибке HTTP
        data = response.json()
        # API возвращает результат в поле 'result'
        return float(data.get("result", 0))
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Ошибка конвертации валюты: {e}")
        return 0.0  # при ошибке возвращаем 0
