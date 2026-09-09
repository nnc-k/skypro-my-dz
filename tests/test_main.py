import pytest
from unittest.mock import patch, MagicMock
from src.main import main


@patch("src.main.read_transactions_csv")
@patch("src.main.read_transactions_excel")
@patch("src.main.read_json_file")
@patch("src.main.filter_by_state")
@patch("src.main.sort_by_date")
@patch("src.main.filter_by_description")
def test_main_full_flow(
    mock_filter_desc,
    mock_sort,
    mock_filter_state,
    mock_read_json,
    mock_read_excel,
    mock_read_csv,
    capsys,
    monkeypatch,
):
    """Тест основного сценария: выбор CSV, фильтр, сортировка, поиск."""
    # Подготавливаем тестовые транзакции
    transactions = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01", "description": "Перевод", "currency": {"code": "RUB"}},
        {"id": 2, "state": "EXECUTED", "date": "2023-12-01", "description": "Оплата", "currency": {"code": "USD"}},
    ]
    mock_read_csv.return_value = transactions
    mock_filter_state.return_value = transactions
    mock_sort.return_value = transactions
    mock_filter_desc.return_value = transactions

    # Подменяем ввод пользователя
    inputs = iter(["2", "EXECUTED", "Нет", "Нет", "Нет"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Запускаем main
    main()

    # Проверяем вывод
    captured = capsys.readouterr()
    assert "Привет! Добро пожаловать" in captured.out
    assert "Для обработки выбран CSV-файл" in captured.out
    assert "Операции отфильтрованы по статусу \"EXECUTED\"" in captured.out
    assert "Распечатываю итоговый список транзакций..." in captured.out
    assert "Всего банковских операций в выборке: 2" in captured.out


@patch("src.main.read_transactions_csv")
@patch("src.main.filter_by_state")
def test_main_no_transactions(mock_filter_state, mock_read_csv, capsys, monkeypatch):
    """Тест, когда транзакции не загружены."""
    mock_read_csv.return_value = []
    inputs = iter(["2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    captured = capsys.readouterr()
    assert "Не удалось загрузить транзакции" in captured.out


@patch("src.main.read_transactions_csv")
@patch("src.main.filter_by_state")
def test_main_empty_result(mock_filter_state, mock_read_csv, capsys, monkeypatch):
    """Тест, когда после фильтрации выборка пуста."""
    transactions = [{"id": 1, "state": "EXECUTED"}]
    mock_read_csv.return_value = transactions
    mock_filter_state.return_value = []  # фильтр вернул пустой список

    inputs = iter(["2", "EXECUTED", "Нет", "Нет", "Нет"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    captured = capsys.readouterr()
    assert "Не найдено ни одной транзакции" in captured.out


def test_invalid_status_retry(capsys, monkeypatch):
    """Тест, что при вводе неверного статуса программа запрашивает повторно."""