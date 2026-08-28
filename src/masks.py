import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""
    digits = card_number.replace(" ", "")

    if len(digits) != 16 or not digits.isdigit():
        logger.error("Некорректный номер карты")
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    result = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    logger.info("Номер банковской карты успешно замаскирован")
    return result


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    digits = account_number.replace(" ", "")

    if len(digits) < 4 or not digits.isdigit():
        logger.error("Некорректный номер счета")
        raise ValueError("Некорректный номер счета.")

    result = f"**{digits[-4:]}"
    logger.info("Номер банковского счета успешно замаскирован")
    return result
