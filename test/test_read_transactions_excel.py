import unittest
from unittest.mock import patch

import pandas as pd

from src.csv_excel_utils import read_transactions_excel


class TestReadTransactionsExcel(unittest.TestCase):
    """
    Класс тестов для функции read_transactions_excel.

    Проверяет корректность считывания финансовых операций
    из Excel-файла и преобразование данных в список словарей.
    """

    @patch("pandas.read_excel")
    def test_read_transactions_excel(self, mock_read_excel) -> None:
        """
        Тестирует функцию read_transactions_excel.

        Проверяет, что данные, считанные из Excel-файла,
        корректно преобразуются в список словарей.
        """

        # Создаём фиктивный DataFrame, как будто он считан из Excel
        mock_df = pd.DataFrame(
            [
                {
                    "ID": 650703,
                    "Status": "EXECUTED",
                    "Date": "2023-09-05T11:30:32Z",
                    "Amount": 16210,
                    "Currency": "Sol",
                    "Code": "PEN",
                    "From": "Счет 58803664561298323391",
                    "To": "Счет 39745660563456619397",
                    "Description": "Перевод организации",
                },
                {
                    "ID": 3598919,
                    "Status": "EXECUTED",
                    "Date": "2020-12-06T23:00:58Z",
                    "Amount": 29740,
                    "Currency": "Peso",
                    "Code": "COP",
                    "From": "Discover 3172601889670065",
                    "To": "Discover 0720428384694643",
                    "Description": "Перевод с карты на карту",
                },
                {
                    "ID": 593027,
                    "Status": "CANCELED",
                    "Date": "2023-07-22T05:02:01Z",
                    "Amount": 30368,
                    "Currency": "Shilling",
                    "Code": "TZS",
                    "From": "Visa 1959232722494097",
                    "To": "Visa 6804119550473710",
                    "Description": "Перевод с карты на карту",
                },
            ]
        )

        mock_read_excel.return_value = mock_df
        expected = mock_df.to_dict(orient="records")

        # Вызываем функцию, она использует mock вместо реального Excel
        result = read_transactions_excel("dummy.xlsx")

        self.assertEqual(result, expected)
        mock_read_excel.assert_called_once_with("dummy.xlsx")


if __name__ == "__main__":
    unittest.main()