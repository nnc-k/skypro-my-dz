# Приложение для банка

## Описание 
Банковское веб-приложение на Python с маскировкой номера карты и счета пользователя

## Установка
1. Клонируйте репозиторий
    ```
   git@github.com:nnc-k/skypro-my-dz.git
   ```
   Перейдите в папку проекта:

```bash
cd python_dz_9_1
```
2. Установите зависимости
```bash
poetry install
```

Активируйте виртуальное окружение:

```bash
poetry shell
```

## Использование
1. Пример работы функции маскировки:

```python
from src.widget import mask_account_card, get_date

print(mask_account_card("Visa Platinum 7000792289606361"))
# Visa Platinum 7000 79** **** 6361

print(mask_account_card("Счет 73654108430135874305"))
# Счет **4305

print(get_date("2024-03-11T02:26:18.671407"))
# 11.03.2024
```

---

## Проверка качества кода

Запуск линтера:

```bash
poetry run flake8
```

Форматирование кода:

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

## Тестирование

Для запуска тестов используйте:

```bash
poetry run pytest
```

---

## Используемые технологии

- Python 3.14
- Poetry
- Pytest
- Flake8
- Black
- isort
- mypy

---