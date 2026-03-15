from typing import Any

def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Возвращает новый список словарей, у которых значение ключа 'state'
    соответствует переданному параметру state.

    :param operations: список словарей с данными об операциях
    :param state: значение состояния для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список словарей
    """
    result: list[dict[str, Any]] = []

    for operation in operations:
        if "state" in operation and operation["state"] == state:
            result.append(operation)

    return result


# Входные данные
operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Вызов функции
result = filter_by_state(operations)

# Вывод
print(result)


from typing import Any

def sort_by_date(operations: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.

    :param operations: список словарей с данными об операциях
    :param reverse: порядок сортировки
                    True — по убыванию (сначала новые даты)
                    False — по возрастанию (сначала старые даты)
    :return: новый список, отсортированный по дате

    Сортировка выполняется с помощью встроенной функции sorted().
    В качестве ключа сортировки используется lambda-функция,
    которая возвращает значение поля 'date' из каждого словаря.
    """
    return sorted(operations, key=lambda op: op["date"], reverse=reverse)
    # key=lambda op: op["date"] означает:    «Сортируй элементы по значению поля date»


    # Входные данные
operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Вызов функции
result = sort_by_date(operations)

# Вывод
print(result)
