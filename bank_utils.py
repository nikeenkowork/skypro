import re
from collections import Counter
from typing import Dict, List


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Ищет транзакции, где в поле 'description' встречается строка поиска.

    Аргументы:
        data (list[dict]): список транзакций
        search (str): строка для поиска в описании

    Возвращает:
        list[dict]: список транзакций, совпадающих с поиском
    """
    # Компилируем регулярное выражение, игнорируя регистр
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    # Фильтруем данные
    result = [txn for txn in data if pattern.search(txn.get("description", ""))]

    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Считает количество операций по заданным категориям.

    Аргументы:
        data (list[dict]): список транзакций, каждая транзакция — словарь
        categories (list[str]): список категорий для подсчета

    Возвращает:
        dict: ключ — категория, значение — количество операций
    """
    # Инициализируем словарь с нулями
    category_counts = {category: 0 for category in categories}

    # Проходим по всем операциям
    for txn in data:
        description = txn.get("description", "")

        for category in categories:
            # Ищем категорию в description (игнорируем регистр)
            if re.search(re.escape(category), description, re.IGNORECASE):
                category_counts[category] += 1

    return category_counts


def count_transaction_categories(transactions, categories):
    """
    Подсчет количества банковских операций по категориям с использованием Counter.

    :param transactions: список словарей с транзакциями
    :param categories: список категорий для подсчета
    :return: словарь {категория: количество операций}
    """
    counter = Counter()
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1
    # добавляем нули для категорий, которых нет
    return {category: counter.get(category, 0) for category in categories}
