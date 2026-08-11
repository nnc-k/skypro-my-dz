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