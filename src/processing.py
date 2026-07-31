def filter_by_state(data: list[dict], state: str = "EXECUTED"
) -> list[dict]:
    """
    Возвращает список словарей с указанным значением state.
    """
    return [item for item in data if item.get("state") == state]