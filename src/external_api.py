# external_api.py
import os

import requests
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму из валюты currency в рубли с помощью API.

    :param amount: сумма в исходной валюте
    :param currency: 'USD', 'EUR' или другая валюта
    :return: сумма в рублях (float)
    """
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
