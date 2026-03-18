from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def test_filter_by_currency_usd():
    # фильтрация по USD
    result = list(filter_by_currency(transactions, "USD"))

    assert result == [
        transactions[0],
        transactions[1],
        transactions[3],
    ]


def test_filter_by_currency_rub():
    # фильтрация по RUB
    result = list(filter_by_currency(transactions, "RUB"))

    assert result == [
        transactions[2],
        transactions[4],
    ]


def test_filter_by_currency_no_matches():
    # Случай, когда нужной валюты нет нужной валюты
    result = list(filter_by_currency(transactions, "EUR"))

    assert result == []


def test_filter_by_currency_empty_list():
    # Пустой список
    result = list(filter_by_currency([], "USD"))

    assert result == []


def test_filter_by_currency_generator_without_errors():
    # отсутствие ошибок, если совпадений нет
    generator = filter_by_currency(transactions, "EUR")
    result = list(generator)

    assert result == []


def test_transaction_descriptions_all_values():
    # возврат всех описаний по порядку
    result = list(transaction_descriptions(transactions))

    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_one_transaction():
    # тестирование с одной транзакцией
    result = list(transaction_descriptions([transactions[0]]))

    assert result == ["Перевод организации"]


def test_transaction_descriptions_empty_list():
    # тестирование пустого списка
    result = list(transaction_descriptions([]))

    assert result == []


def test_card_number_generator_basic_range():
    # правильная генерация диапазона
    result = list(card_number_generator(1, 3))

    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_card_number_generator_format():
    # корректный формат XXXX XXXX XXXX XXXX
    card = next(card_number_generator(1, 1))

    parts = card.split()

    assert len(parts) == 4
    assert all(len(part) == 4 for part in parts)
    assert all(part.isdigit() for part in parts)


def test_card_number_generator_boundaries():
    # крайние значения (границы диапазона)
    result = list(card_number_generator(9998, 10000))

    assert result == [
        "0000 0000 0000 9998",
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
    ]
