import json
import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    LOG_DIR / "utils.log",
    mode="w",
    encoding="utf-8",
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def read_json_file(file_path: str) -> list[dict]:
    """Читает JSON-файл и возвращает список словарей."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info("JSON-файл %s успешно прочитан", file_path)
            return data

        logger.error(
            "JSON-файл %s содержит данные не в виде списка",
            file_path,
        )
        return []

    except FileNotFoundError:
        logger.error("JSON-файл %s не найден", file_path)
        return []

    except json.JSONDecodeError:
        logger.error(
            "Ошибка декодирования JSON-файла %s",
            file_path,
        )
        return []
