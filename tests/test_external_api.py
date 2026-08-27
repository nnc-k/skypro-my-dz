from unittest.mock import Mock, patch

from src.external_api import convert_to_rub


def test_convert_to_rub():
    """Проверяет транзакцию в рублях."""
    transaction = {
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "code": "RUB",
                "name": "руб.",
            },
        },
    }

    with patch("src.external_api.requests.get") as mock_get:
        result = convert_to_rub(transaction)

    assert result == 1000.0
    mock_get.assert_not_called()


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    """Проверяет конвертацию долларов в рубли."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "result": 9000.0,
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "USD",
                "name": "USD",
            },
        },
    }

    result = convert_to_rub(transaction)

    assert result == 9000.0

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        params={
            "to": "RUB",
            "from": "USD",
            "amount": 100.0,
        },
        headers={"apikey": mock_get.call_args.kwargs["headers"]["apikey"]},
    )


@patch("src.external_api.requests.get")
def test_convert_eur_to_rub(mock_get):
    """Проверяет конвертацию евро в рубли."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "result": 10500.0,
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "EUR",
                "name": "EUR",
            },
        },
    }

    result = convert_to_rub(transaction)

    assert result == 10500.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_error(mock_get):
    """Проверяет обработку ошибки API."""
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "USD",
                "name": "USD",
            },
        },
    }

    with pytest.raises(requests.exceptions.HTTPError):
        convert_to_rub(transaction)
