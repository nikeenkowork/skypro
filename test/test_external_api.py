import os
import sys

from external_api import convert_to_rub

# Добавляем путь к папке src, где лежит external_api.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


# Тестовая конвертация
amount = 100
currency = "EUR"

result = convert_to_rub(amount, currency)

if result > 0:
    print(f"✅ API работает! {amount} {currency} = {result} RUB")
else:
    print("❌ Ошибка: проверьте ключ API и URL")
