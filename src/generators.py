from typing import Iterator


def filter_by_currency(
    transactions: list[dict], currency: str
) -> Iterator[dict]:
    """Возвращает транзакции только с указанной валютой."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(
    transactions: list[dict],
) -> Iterator[str]:
    """Поочередно возвращает описания транзакций."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int):
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield " ".join(card_number[i:i + 4] for i in range(0, 16, 4))