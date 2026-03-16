import pytest
from src.processing import sort_by_date


@pytest.fixture
def operations() -> list[dict[str, int | str]]:
    return [
        {"id": 1, "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "date": "2018-10-14T08:21:33.419441"},
    ]

# Тест сортировки
@pytest.mark.parametrize(
    "reverse, expected_ids",
    [
        (True, [1, 4, 3, 2]),   # по убыванию
        (False, [2, 3, 4, 1]),  # по возрастанию
    ],
)
def test_sort_by(
    operations: list[dict[str, int | str]],
    reverse: bool,
    expected_ids: list[int],
) -> None:
    result = sort_by_date(operations, reverse)

    result_ids = [operation["id"] for operation in result]

    assert result_ids == expected_ids


# Тест одинаковых дат
def test_sort_by_date_sam() -> None:
    operations = [
        {"id": 1, "date": "2020-01-01T10:00:00"},
        {"id": 2, "date": "2020-01-01T10:00:00"},
        {"id": 3, "date": "2021-01-01T10:00:00"},
    ]

    result = sort_by_date(operations)

    result_ids = [operation["id"] for operation in result]

    assert result_ids[0] == 3

# Тест одинаковых дат
def test_sort_by_date_format() -> None:
    operations = [
        {"id": 1, "date": "invalid-date"},
        {"id": 2, "date": "2019-07-03T18:35:29.512364"},
    ]

    result = sort_by_date(operations)

    assert isinstance(result, list)