import pytest
from bank_utils import count_transaction_categories, process_bank_operations, process_bank_search

data = [
    {"id": 1, "description": "Оплата в магазине"},
    {"id": 2, "description": "перевод другу"},
    {"id": 3, "description": "Зарплата"},
    {"id": 4, "description": "оплата коммунальных услуг"},
    {"id": 5, "description": ""},
]


# -------- Тесты для process_bank_search --------
@pytest.mark.parametrize(
    "search, expected_ids",
    [
        ("оплата", {1, 4}),
        ("ЗАРПЛАТА", {3}),
        ("подарок", set()),
        ("", {1, 2, 3, 4, 5}),
    ],
)
def test_process_bank_search(search, expected_ids):
    result = process_bank_search(data, search)
    assert {txn["id"] for txn in result} == expected_ids


# -------- Тесты для process_bank_operations --------
@pytest.mark.parametrize(
    "categories, expected_counts",
    [
        (["оплата", "зарплата"], {"оплата": 2, "зарплата": 1}),
        (["перевод"], {"перевод": 1}),
        (["подарок"], {"подарок": 0}),
        ([], {}),
    ],
)
def test_process_bank_operations(categories, expected_counts):
    result = process_bank_operations(data, categories)
    assert result == expected_counts


# -------- Тесты для count_transaction_categories --------
@pytest.mark.parametrize(
    "categories, expected_counts",
    [
        (["оплата", "зарплата"], {"оплата": 2, "зарплата": 1}),
        (["перевод"], {"перевод": 1}),
        (["подарок"], {"подарок": 0}),
        ([], {}),
    ],
)
def test_count_transaction_categories(categories, expected_counts):
    result = count_transaction_categories(data, categories)
    assert result == expected_counts
