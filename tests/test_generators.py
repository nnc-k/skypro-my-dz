import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def transactions():
    """Возвращает тестовые данные транзакций."""
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "USD"},
            },
            "description": "Покупка в магазине",
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200",
                "currency": {"code": "EUR"},
            },
            "description": "Перевод средств",
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300",
                "currency": {"code": "USD"},
            },
            "description": "Оплата услуг",
        },
    ]


@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [1, 3]),
        ("EUR", [2]),
        ("GBP", []),
    ],
)
def test_filter_by_currency(transactions, currency, expected_ids):
    """Проверяет фильтрацию транзакций по валюте."""
    result = list(filter_by_currency(transactions, currency))

    assert [transaction["id"] for transaction in result] == expected_ids


def test_transaction_descriptions(transactions):
    """Проверяет получение описаний транзакций."""
    result = list(transaction_descriptions(transactions))

    assert result == [
        "Покупка в магазине",
        "Перевод средств",
        "Оплата услуг",
    ]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (
                9999,
                10001,
                [
                    "0000 0000 0000 9999",
                    "0000 0000 0001 0000",
                    "0000 0000 0001 0001",
                ],
        ),
    ],
)
def test_card_number_generator(start, stop, expected):
    """Проверяет генерацию номеров банковских карт."""
    result = list(card_number_generator(start, stop))

    assert result == expected