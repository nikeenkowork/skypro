def get_mask_card_number(card_number: int | str) -> str:
    """
    Функция маскирует номер банковской карты.
    """
    bank_card = str(card_number)
    if not bank_card:
        return ""

    if len(bank_card) == 16 and bank_card.isdigit():
        return f"{bank_card[:4]} {bank_card[4:6]}** **** {bank_card[-4:]}"
    return bank_card


def get_mask_account(account_number: int | str) -> str:
    """
    Функция маскирует номер банковского счета.
    """
    account_str = str(account_number)

    if not account_str:
        return ""
    return f"**{account_str[-4:]}"
