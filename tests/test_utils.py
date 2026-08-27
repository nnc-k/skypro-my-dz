from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file():
    """Проверяет успешное чтение JSON-файла."""
    json_data = '[{"amount": "100", "currency": "USD"}]'

    with patch("builtins.open", mock_open(read_data=json_data)):
        result = read_json_file("operations.json")

    assert result == [{"amount": "100", "currency": "USD"}]


def test_read_json_file_empty():
    """Проверяет чтение пустого JSON-файла."""
    with patch("builtins.open", mock_open(read_data="")):
        result = read_json_file("operations.json")

    assert result == []


def test_read_json_file_not_list():
    """Проверяет JSON-файл, содержащий не список."""
    json_data = '{"amount": "100", "currency": "USD"}'

    with patch("builtins.open", mock_open(read_data=json_data)):
        result = read_json_file("operations.json")

    assert result == []


def test_read_json_file_not_found():
    """Проверяет обработку отсутствующего файла."""
    with patch(
        "builtins.open",
        side_effect=FileNotFoundError,
    ):
        result = read_json_file("operations.json")

    assert result == []


def test_read_json_file_invalid_json():
    """Проверяет обработку некорректного JSON."""
    json_data = '{"amount": "100", "currency": }'

    with patch("builtins.open", mock_open(read_data=json_data)):
        result = read_json_file("operations.json")

    assert result == []

