import os
import requests
from dotenv import load_dotenv

# загружаем переменные из .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_transaction_to_rub(transaction: dict) -> float:
    """
    Конвертирует транзакцию из валюты transaction['operationAmount']['currency']['code'] в рубли.
    При пустой или некорректной транзакции возвращает 0.
    """
    op_amount = transaction.get("operationAmount")
    if not op_amount:
        return 0.0  # пропускаем пустые транзакции

    amount_str = op_amount.get("amount")
    currency_info = op_amount.get("currency", {})
    currency_code = currency_info.get("code", "RUB")

    if amount_str is None:
        return 0.0

    try:
        amount = float(amount_str)
    except (ValueError, TypeError):
        return 0.0

    if currency_code.upper() == "RUB":
        return amount  # уже в рублях

    params = {"from": currency_code.upper(), "to": "RUB", "amount": amount}
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(BASE_URL, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return float(data.get("result", 0))
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Ошибка конвертации валюты: {e}")
        return 0.0
