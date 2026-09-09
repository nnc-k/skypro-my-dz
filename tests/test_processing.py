import pytest

from src.processing import (
    count_by_category,
    filter_by_description,
    filter_by_state,
    sort_by_date,
)


@pytest.fixture
def operations():
    """Фикстура с тестовыми транзакциями."""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2024-03-11T10:00:00",
            "description": "Перевод на карту",
            "currency": {"code": "RUB"},
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2023-07-15T14:30:00",
            "description": "Оплата услуг",
            "currency": {"code": "USD"},
        },
        {
            "id": 3,
            "state": "CANCELED",
            "date": "2022-05-05T09:30:00",
            "description": "Перевод на счет",
            "currency": {"code": "RUB"},
        },
        {
            "id": 4,
            "state": "PENDING",
            "date": "2024-01-01T12:00:00",
            "description": "Покупка в магазине",
            "currency": {"code": "EUR"},
        },
    ]


# ------------------ Тесты для filter_by_state ------------------
def test_filter_by_state_default(operations):
    result = filter_by_state(operations)
    assert len(result) == 2
    assert result[0]["state"] == "EXECUTED"


def test_filter_by_state_cancelled(operations):
    result = filter_by_state(operations, "CANCELED")
    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"


# ------------------ Тесты для sort_by_date ------------------
def test_sort_by_date_desc(operations):
    result = sort_by_date(operations)
    assert result[0]["date"] == "2024-03-11T10:00:00"
    assert result[-1]["date"] == "2022-05-05T09:30:00"


def test_sort_by_date_asc(operations):
    result = sort_by_date(operations, reverse=False)
    assert result[0]["date"] == "2022-05-05T09:30:00"
    assert result[-1]["date"] == "2024-03-11T10:00:00"


# ------------------ Тесты для filter_by_description ------------------
def test_filter_by_description_found(operations):
    result = filter_by_description(operations, "перевод")
    assert len(result) == 2
    assert all("перевод" in t["description"].lower() for t in result)


def test_filter_by_description_not_found(operations):
    result = filter_by_description(operations, "несуществующее")
    assert result == []


def test_filter_by_description_case_insensitive(operations):
    result = filter_by_description(operations, "ПЕРЕВОД")
    assert len(result) == 2


# ------------------ Тесты для count_by_category ------------------
def test_count_by_category(operations):
    categories = ["Перевод на карту", "Оплата услуг", "Неизвестная"]
    result = count_by_category(operations, categories)
    expected = {"Перевод на карту": 1, "Оплата услуг": 1, "Неизвестная": 0}
    assert result == expected


def test_count_by_category_empty():
    assert count_by_category([], ["A"]) == {"A": 0}
