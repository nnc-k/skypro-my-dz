import re
from collections import Counter
from typing import Any, Dict, List


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Возвращает список словарей с указанным значением state.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате.

    :param data: список словарей с ключом "date"
    :param reverse: порядок сортировки.
                    True — по убыванию (по умолчанию),
                    False — по возрастанию.
    :return: отсортированный список словарей.
    """
    return sorted(data, key=lambda item: item["date"], reverse=reverse)


def filter_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по наличию строки поиска в описании (поле 'description').

    Аргументы:
        transactions: список словарей с транзакциями.
        search_string: строка для поиска (регистронезависимо).

    Возвращает:
        список транзакций, у которых в описании найдена искомая строка.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def count_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по категориям (поле 'description').

    Аргументы:
        transactions: список словарей с транзакциями.
        categories: список категорий (строк) для подсчёта.

    Возвращает:
        словарь {категория: количество}, для отсутствующих категорий – 0.
    """
    descriptions = [t.get("description", "") for t in transactions]
    counter = Counter(descriptions)
    return {cat: counter.get(cat, 0) for cat in categories}
