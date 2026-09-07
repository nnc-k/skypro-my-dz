"""Чтение финансовых операций из CSV- и XLSX-файлов."""

from pathlib import Path
from typing import Any, cast

import pandas as pd

FilePath = str | Path
Transaction = dict[str, Any]


def read_transactions_csv(file_path: FilePath) -> list[Transaction]:
    """Прочитать CSV-файл и вернуть список словарей с транзакциями."""
    dataframe = pd.read_csv(file_path)
    return cast(list[Transaction], dataframe.to_dict(orient="records"))


def read_transactions_excel(file_path: FilePath) -> list[Transaction]:
    """Прочитать первый лист XLSX-файла и вернуть список транзакций."""
    dataframe = pd.read_excel(file_path, engine="openpyxl")
    return cast(list[Transaction], dataframe.to_dict(orient="records"))