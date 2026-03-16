import pytest
from src.processing import filter_by_state


@pytest.fixture
def operations() -> list[dict[str, int | str]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 2, "state": "CANCELED", "date": "2018-06-30"},
        {"id": 3, "state": "EXECUTED", "date": "2018-09-12"},
    ]


def test_filter_by_state_executed(
    operations: list[dict[str, int | str]],
) -> None:
    result = filter_by_state(operations, "EXECUTED")

    assert result == [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 3, "state": "EXECUTED", "date": "2018-09-12"},
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state_parametrize(
    operations: list[dict[str, int | str]],
    state: str,
    expected_ids: list[int],
) -> None:
    result = filter_by_state(operations, state)

    result_ids = [operation["id"] for operation in result]

    assert result_ids == expected_ids