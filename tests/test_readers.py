"""Тесты чтения транзакций из CSV- и XLSX-файлов."""

from pathlib import Path
from typing import Any
from unittest.mock import Mock, patch

import pytest

# Импортируем функции из модуля
from src.file_readers import read_transactions_csv, read_transactions_excel


@pytest.mark.parametrize("use_path_object", [False, True])
def test_read_transactions_csv(use_path_object: bool) -> None:
    """CSV читается по строковому пути и объекту Path."""
    file_path = Path("transactions.csv")
    argument = file_path if use_path_object else str(file_path)

    # Подготовка фиктивных данных
    transactions: list[dict[str, Any]] = [
        {"id": 1, "amount": 1500, "currency_code": "RUB"},
        {"id": 2, "amount": 250, "currency_code": "USD"},
    ]
    dataframe = Mock()
    dataframe.to_dict.return_value = transactions

    # Патчим pd.read_csv внутри модуля src.file_readers
    with patch("src.file_readers.pd.read_csv", return_value=dataframe) as mock_read_csv:
        result = read_transactions_csv(argument)

    assert result == transactions
    mock_read_csv.assert_called_once_with(argument)  # без sep
    dataframe.to_dict.assert_called_once_with(orient="records")


@pytest.mark.parametrize("use_path_object", [False, True])
def test_read_transactions_excel(use_path_object: bool) -> None:
    """XLSX читается по строковому пути и объекту Path."""
    file_path = Path("transactions_excel.xlsx")
    argument = file_path if use_path_object else str(file_path)

    transactions: list[dict[str, Any]] = [
        {"id": 1, "amount": 1500, "currency_code": "RUB"},
        {"id": 2, "amount": 250, "currency_code": "USD"},
    ]
    dataframe = Mock()
    dataframe.to_dict.return_value = transactions

    with patch("src.file_readers.pd.read_excel", return_value=dataframe) as mock_read_excel:
        result = read_transactions_excel(argument)

    assert result == transactions
    mock_read_excel.assert_called_once_with(argument, engine="openpyxl")
    dataframe.to_dict.assert_called_once_with(orient="records")


def test_read_transactions_csv_without_rows() -> None:
    """CSV с заголовками, но без строк данных возвращает пустой список."""
    dataframe = Mock()
    dataframe.to_dict.return_value = []

    with patch("src.file_readers.pd.read_csv", return_value=dataframe):
        assert read_transactions_csv("empty.csv") == []


def test_read_transactions_excel_without_rows() -> None:
    """Excel без строк данных возвращает пустой список."""
    dataframe = Mock()
    dataframe.to_dict.return_value = []

    with patch("src.file_readers.pd.read_excel", return_value=dataframe):
        assert read_transactions_excel("empty.xlsx") == []


def test_read_transactions_csv_missing_file() -> None:
    """Ошибка отсутствия CSV-файла передаётся вызывающему коду."""
    with patch("src.file_readers.pd.read_csv") as mock_read_csv:
        mock_read_csv.side_effect = FileNotFoundError("Файл не найден")
        with pytest.raises(FileNotFoundError):
            read_transactions_csv("missing.csv")


def test_read_transactions_excel_missing_file() -> None:
    """Ошибка отсутствия Excel-файла передаётся вызывающему коду."""
    with patch("src.file_readers.pd.read_excel") as mock_read_excel:
        mock_read_excel.side_effect = FileNotFoundError("Файл не найден")
        with pytest.raises(FileNotFoundError):
            read_transactions_excel("missing.xlsx")
