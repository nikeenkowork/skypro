import pytest

from src.widget import get_date


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("1999-12-31T23:59:59.000000", "31.12.1999"),
        ("2000-01-01T00:00:00.000000", "01.01.2000"),
    ],
)
def test_get_date_standard_format(value: str, expected: str) -> None:
    assert get_date(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("2023-05-15", "15.05.2023"),
        ("2020-02-29", "29.02.2020"),
    ],
)
def test_get_date_short_format(value: str, expected: str) -> None:
    assert get_date(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        "",
        "text",
        "2023",
        "date not found",
    ],
)
def test_get_date_invalid_strings(value: str) -> None:
    result = get_date(value)
    assert isinstance(result, str)
