import logging

# Создание логера для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler("masks.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Формат логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Установка форматтера
file_handler.setFormatter(file_formatter)

# Добавление handler к логеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """
    Функция маскирует номер банковской карты.
    """
    bank_card = str(card_number)

    if not bank_card:
        logger.error("Передан пустой номер карты")
        return ""

    if len(bank_card) == 16 and bank_card.isdigit():
        masked = f"{bank_card[:4]} {bank_card[4:6]}** **** {bank_card[-4:]}"
        logger.debug(f"Карта успешно замаскирована: {masked}")
        return masked

    logger.error(f"Некорректный номер карты: {card_number}")
    return bank_card


def get_mask_account(account_number: int | str) -> str:
    """
    Функция маскирует номер банковского счета.
    """
    account_str = str(account_number)

    if not account_str:
        logger.error("Передан пустой номер счета")
        return ""

    masked = f"**{account_str[-4:]}"
    logger.debug(f"Счет успешно замаскирован: {masked}")
    return masked
