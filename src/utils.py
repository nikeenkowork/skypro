import json
import logging
from typing import Dict, List

# Создаём логгер для модуля
logger = logging.getLogger(__name__)


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает финансовые транзакции из JSON-файла.

    :param file_path: путь до JSON-файла
    :return: список словарей с транзакциями, или пустой список при ошибке
    """
    try:
        logger.info(f"Попытка открыть файл: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        logger.info(f"Файл успешно прочитан: {file_path}")
        return data
        # Предполагаем, что data — это список словарей

    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Файл не найден: {file_path}")
        return []

    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
