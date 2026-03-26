import json
from typing import Dict, List


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает финансовые транзакции из JSON-файла.

    :param file_path: путь до JSON-файла
    :return: список словарей с транзакциями, или пустой список при ошибке
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Предполагаем, что data — это список словарей
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
