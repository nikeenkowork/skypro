import requests

url = "https://api.apilayer.com/exchangerates_data/convert"

headers = {"apikey": "iNJjtsrCm8C6dmn9rsjbd42geeVAWmVD"}

params = {"from": "USD", "to": "EUR", "amount": 100}

response = requests.get(url, headers=headers, params=params)

print(response.json())
