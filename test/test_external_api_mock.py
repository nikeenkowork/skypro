import os
import sys
from unittest.mock import Mock, patch

from src.external_api import convert_transaction_to_rub

# Добавляем папку src в путь поиска модулей
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


def test_convert_usd_to_rub():
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    with patch("src.external_api.requests.get") as mock_get, patch("src.external_api.API_KEY", "dummy_key"):
        mock_response = Mock()
        mock_response.json.return_value = {"result": 8000}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Передаём два аргумента, как требует функция
        result = convert_transaction_to_rub(transaction)

    assert result == 8000.0
