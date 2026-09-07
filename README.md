# Приложение для банка

## Описание

Проект разработан в рамках курса **SkyPro "Python-разработчик"**.

Приложение предоставляет функции для обработки банковских операций:

- маскировка номеров банковских карт;
- маскировка номеров банковских счетов;
- определение типа платежного инструмента (карта или счет);
- форматирование даты;
- фильтрация и сортировка банковских операций.
- фильтрация транзакций по валюте;
- получение описаний транзакций;
- генерация номеров банковских карт в заданном диапазоне.

---

## Установка

Клонируйте репозиторий:

```bash
git clone <ссылка_на_репозиторий>
```

Перейдите в директорию проекта:

```bash
cd python_dz_9_1
```

### Установка зависимостей с помощью Poetry

```bash
poetry install
```

Активируйте виртуальное окружение:

```bash
poetry shell
```

### Альтернативная установка через pip

```bash
pip install -r requirements.txt
```

---

## Требования

- Python 3.14 или выше
- Poetry 2.x (рекомендуется)

---

## Использование

```python
from src.widget import mask_account_card, get_date

# Маскировка номера банковской карты
print(mask_account_card("Visa Platinum 7000792289606361"))
# Visa Platinum 7000 79** **** 6361

# Маскировка номера банковского счета
print(mask_account_card("Счет 73654108430135874305"))
# Счет **4305

# Форматирование даты
print(get_date("2024-03-11T02:26:18.671407"))
# 11.03.2024

from src.generators import ( filter_by_currency, transaction_descriptions, card_number_generator, ) 

# Фильтрация транзакций по валюте 
for transaction in filter_by_currency(transactions, "USD"): 
    print(transaction) 
    
# Получение описаний транзакций 
for description in transaction_descriptions(transactions): 
    print(description)
    
# Генерация номеров банковских карт 
for card_number in card_number_generator(1, 5): 
    print(card_number)
```
## Декоратор log

Декоратор `log` используется для логирования выполнения функций.

Лог может выводиться:
- в консоль, если `filename` не указан;
- в файл, если указан параметр `filename`.

При успешном выполнении функции записывается сообщение с её именем.
При возникновении ошибки записываются имя функции, тип ошибки и входные параметры.
---
## Новое: чтение CSV и Excel

Добавлены функции для чтения финансовых транзакций из файлов CSV и Excel (.xlsx) в модуле `src/file_readers.py`:
- `read_transactions_csv(file_path)` — читает CSV, возвращает список словарей.
- `read_transactions_excel(file_path)` — читает Excel, возвращает список словарей.

Пример:
```python
from src.file_readers import read_transactions_csv, read_transactions_excel
csv_data = read_transactions_csv('data/transactions.csv')
excel_data = read_transactions_excel('data/transactions_excel.xlsx')

## Проверка качества кода

#Проверка стиля кода:

```bash
poetry run flake8
```

Форматирование:

```bash
poetry run black .
```

Сортировка импортов:

```bash
poetry run isort .
```

Проверка типов:

```bash
poetry run mypy src
```

---

## Запуск тестов

```bash
poetry run pytest
```
## Покрытие тестами

Для запуска тестов и формирования отчета покрытия выполните:

```bash
poetry run pytest --cov=src --cov-report=html
```

После выполнения будет создана папка `htmlcov` с HTML-отчетом. Откройте файл `htmlcov/index.html` в браузере для просмотра результатов.
---

## Используемые технологии

- Python 3.14
- Poetry
- Pytest
- Flake8
- Black
- isort
- mypy