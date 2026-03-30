import os
import sys

from src.external_api import convert_transaction_to_rub  # теперь Python видит модуль

# Добавляем путь к папке src, где лежит external_api.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# Тестовая конвертация
amount = 100
currency = "EUR"

tx = {"amount": amount, "currency": currency}
result = convert_transaction_to_rub(tx)


if result > 0:
    print(f"✅ API работает! {amount} {currency} = {result} RUB")
else:
    print("❌ Ошибка: проверьте ключ API и URL")
