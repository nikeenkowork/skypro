import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Classic 1234567812345678", "Visa Classic **** **** **** 5678"),
        ("Visa Gold 1111222233334444", "Visa Gold **** **** **** 4444"),
        ("Maestro 1234567890123456", "Maestro **** **** **** 3456"),
        ("MasterCard 5555666677778888", "MasterCard **** **** **** 8888"),
    ],
)
def test_mask_account_card_for_cards(data: str, expected: str) -> None:
    assert mask_account_card(data) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Счет 11112222333344445555", "Счет **5555"),
        ("Счет 1234567890123456", "Счет **3456"),
    ],
)
def test_mask_account_card_for_accounts(data: str, expected: str) -> None:
    assert mask_account_card(data) == expected


@pytest.mark.parametrize(
    "data",
    [
        "",
        "Просто текст",
        "Visa Classic",
        "1234567812345678",
        "Счет",
        "Счет ABCDEFGH",
        "Visa Classic 1234",
        "Maestro 1234 5678 9012 3456",
        "Карта 123456789012345",
    ],
)
def test_mask_account_card_invalid_data(data: str) -> None:
    assert mask_account_card(data) == "Некорректные данные"
