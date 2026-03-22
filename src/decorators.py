from functools import wraps

def log(filename=None):
    """
    Декоратор для логирования работы функции.

    Логирует:
    - успешное выполнение функции (имя + результат)
    - ошибки (тип ошибки + входные аргументы)

    Логи выводятся:
    - в консоль (всегда)
    - в файл (если передан filename)

    :param filename: имя файла для записи логов (str или None)
    :return: декоратор
    """
    def decorator(func):
        """
        Оборачивает функцию для добавления логирования.

        :param func: декорируемая функция
        :return: wrapper-функция
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Выполняет функцию с логированием.

            :param args: позиционные аргументы функции
            :param kwargs: именованные аргументы функции
            :return: результат функции или None при ошибке
            """
            try:
                result = func(*args, **kwargs)

                message = f"{func.__name__} ok, result={result}"

                print(message)

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")

                return result

            except Exception as e:
                error_message = (
                    f"{func.__name__} error: {type(e).__name__}, "
                    f"inputs={args}, {kwargs}"
                )

                print(error_message)

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")

                return None

        return wrapper
    return decorator
