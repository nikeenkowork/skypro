def filter_by_currency(transactions, currency):
    """
    Генератор, который возвращает транзакции с заданной валютой.

    :param transactions: список словарей с транзакциями
    :param currency: код валюты (например, 'USD')
    :return: итератор транзакций
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой транзакции.

    :param transactions: список словарей с транзакциями
    :return: итератор описаний
    """
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, end):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    Для каждого числа в диапазоне от start до end (включительно)
    возвращает строку длиной 16 символов, дополненную нулями слева
    при необходимости, и разбитую на группы по 4 цифры.

    Args:
        start (int): Начальное значение диапазона.
        end (int): Конечное значение диапазона (включительно).

    Yields:
        str: Номер карты в формате 'XXXX XXXX XXXX XXXX'.

    Example:
        >>> list(card_number_generator(1, 3))
        ['0000 0000 0000 0001',
         '0000 0000 0000 0002',
         '0000 0000 0000 0003']
    """
    for number in range(start, end + 1):
        s = f"{number:016d}"
        # 'd' означает целое число (decimal)
        # '016' 16 → длина строки = 16 символов
        # 0 → если не хватает цифр → добавить нули слева
        yield " ".join(s[i : i + 4] for i in range(0, 16, 4))
        # разбиваем на группы по 4
