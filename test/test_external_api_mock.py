import os
import sys

# test/test_external_api.py
from unittest.mock import Mock, patch

from external_api import convert_to_rub

# Добавляем папку src в путь поиска модулей
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


@patch("external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"result": 8000}
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    result = convert_to_rub(100, "USD")

    assert result == 8000.0
