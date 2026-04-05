import csv

import pandas as pd


def read_transactions_csv(file_path):
    """
    Считывает финансовые операции из CSV.

    Аргументы:
        file_path (str++): путь к CSV файлу

    Возвращает:
        list[dict]: список словарей с транзакциями
    """
    transactions = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions


def read_transactions_excel(file_path):
    """
    Считывает финансовые операции из Excel.

    Аргументы:
        file_path (str): путь к Excel файлу (.xlsx, .xls)

    Возвращает:
        list[dict]: список словарей с транзакциями
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


# Пример использования
# if __name__ == "__main__":
#     csv_transactions = read_transactions_csv("transactions.csv")
#     excel_transactions = read_transactions_excel("transactions_excel.xlsx")
#
#     print("CSV:", csv_transactions[:3])  # первые 3 записи для примера
#     print("Excel:", excel_transactions[:3])
