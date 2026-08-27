import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли."""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_RATES_API_KEY")


    url = "https://api.apilayer.com/exchangerates_data/convert"

    response = requests.get(
        url,
        params={
            "to": "RUB",
            "from": currency,
            "amount": amount,
        },
        headers={"apikey": api_key},
    )

    response.raise_for_status()

    data = response.json()

    return float(data["result"])
