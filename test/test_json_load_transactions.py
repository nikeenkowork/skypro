import os
import sys
from unittest.mock import mock_open, patch
from src.utils import load_transactions  # добавляем src в путь поиска модулей

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


def test_load_transactions_success():
    fake_json = '[{"amount": 100, "currency": "USD"}, {"amount": 200, "currency": "RUB"}]'

    with patch("builtins.open", mock_open(read_data=fake_json)):
        result = load_transactions("data.json")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["amount"] == 100
    assert result[1]["currency"] == "RUB"
