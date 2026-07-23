from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета.
    """

    name, number = data.rsplit(" ", 1)

    if name == "Счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """
    Возвращает дату в формате ДД.ММ.ГГГГ.
    """

    date = datetime.fromisoformat(date_string)
    return date.strftime("%d.%m.%Y")

