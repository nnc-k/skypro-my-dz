def filter_by_state(data: list[dict], state: str = "EXECUTED"
) -> list[dict]:
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