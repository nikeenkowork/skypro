# main.py
import json

from bank_utils import process_bank_search
from data import transactions_csv, transactions_excel


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            file_path = input("Введите путь к JSON-файлу: ").strip()
            try:
                with open(file_path, encoding="utf-8") as f:
                    transactions = json.load(f)
                break
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            file_path = input("Введите путь к CSV-файлу: ").strip()
            try:
                transactions = transactions_csv(file_path)
                break
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            file_path = input("Введите путь к Excel-файлу: ").strip()
            try:
                transactions = transactions_excel(file_path)
                break
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")
        else:
            print("Неверный выбор. Попробуйте снова.")

    # Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status_input = (
            input(
                f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
                f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}\n"
            )
            .strip()
            .upper()
        )
        if status_input in valid_statuses:
            filtered = [t for t in transactions if t.get("status", "").upper() == status_input]
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        order_choice = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = order_choice in ["по убыванию", "убыванию"]
        filtered.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    # Фильтрация по валюте (рубли)
    rub_filter = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rub_filter == "да":
        filtered = [t for t in filtered if t.get("amount", "").endswith("руб.")]

    # Фильтрация по описанию
    desc_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if desc_filter == "да":
        keyword = input("Введите слово для фильтрации: ").strip()
        filtered = process_bank_search(filtered, keyword)

    # Вывод итогового списка
    print("Распечатываю итоговый список транзакций...\n")
    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered)}\n")
    for t in filtered:
        date = t.get("date", "")
        description = t.get("description", "")
        from_acc = t.get("from", "")
        to_acc = t.get("to", "")
        amount = t.get("amount", "")
        print(f"{date} {description}")
        if from_acc or to_acc:
            print(f"{from_acc} -> {to_acc}")
        print(f"Сумма: {amount}\n")


if __name__ == "__main__":
    main()
