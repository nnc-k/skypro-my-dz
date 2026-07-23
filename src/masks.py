def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты"""
    digits = card_number.replace(" ", "")

    if len(digits) != 16 or not digits.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    return f"{digits[:4]} " f"{digits[4:6]}** " f"**** " f"{digits[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    digits = account_number.replace(" ", "")

    if len(digits) < 4 or not digits.isdigit():
        raise ValueError("Некорректный номер счета.")

    return f"**{digits[-4:]}"
