import unittest
from unittest.mock import mock_open, patch

from src.csv_excel_utils import read_transactions_csv


class TestReadTransactionsCSV(unittest.TestCase):
    """Тесты для функции считывания финансовых операций из CSV."""

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=(
            "ID,Status,Date,Amount,Currency,Code,From,To,Description\n"
            "650703,EXECUTED,2023-09-05T11:30:32Z,16210,Sol,PEN,Счет 58803664561298323391,Счет 39745660563456619397,Перевод организации\n"
            "3598919,EXECUTED,2020-12-06T23:00:58Z,29740,Peso,COP,Discover 3172601889670065,Discover 0720428384694643,Перевод с карты на карту\n"
            "593027,CANCELED,2023-07-22T05:02:01Z,30368,Shilling,TZS,Visa 1959232722494097,Visa 6804119550473710,Перевод с карты на карту"
        ),
    )
    def test_read_transactions_csv(self, mock_file) -> None:
        """Проверяет корректное считывание транзакций из CSV-файла."""

        expected = [
            {
                "ID": "650703",
                "Status": "EXECUTED",
                "Date": "2023-09-05T11:30:32Z",
                "Amount": "16210",
                "Currency": "Sol",
                "Code": "PEN",
                "From": "Счет 58803664561298323391",
                "To": "Счет 39745660563456619397",
                "Description": "Перевод организации",
            },
            {
                "ID": "3598919",
                "Status": "EXECUTED",
                "Date": "2020-12-06T23:00:58Z",
                "Amount": "29740",
                "Currency": "Peso",
                "Code": "COP",
                "From": "Discover 3172601889670065",
                "To": "Discover 0720428384694643",
                "Description": "Перевод с карты на карту",
            },
            {
                "ID": "593027",
                "Status": "CANCELED",
                "Date": "2023-07-22T05:02:01Z",
                "Amount": "30368",
                "Currency": "Shilling",
                "Code": "TZS",
                "From": "Visa 1959232722494097",
                "To": "Visa 6804119550473710",
                "Description": "Перевод с карты на карту",
            },
        ]

        result = read_transactions_csv("dummy.csv")
        self.assertEqual(result, expected)
        mock_file.assert_called_once_with("dummy.csv", newline="", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()