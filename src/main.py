from typing import List

from src.file_readers import read_transactions_csv, read_transactions_excel
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.utils import read_json_file

VALID_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def get_user_choice(prompt: str, options: List[str]) -> str:
    """Запрашивает у пользователя выбор из списка и возвращает корректный вариант."""
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print(f"Некорректный ввод. Доступные варианты: {', '.join(options)}")


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = get_user_choice("Ваш выбор: ", ["1", "2", "3"])

    # Загрузка данных (JSON пока заглушка)
    transactions = []
    if choice == "2":
        transactions = read_transactions_csv("data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        transactions = read_transactions_excel("data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    elif choice == "1":
        transactions = read_json_file("data/operations.json")
        print("Чтение JSON пока не реализовано в этом примере.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции.")
        return

    # Фильтрация по статусу (используем существующую функцию)
    while True:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .upper()
        )
        if status in VALID_STATUSES:
            break
        print(f'Статус операции "{status}" недоступен.')

    filtered = filter_by_state(transactions, state=status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    # Сортировка по дате (используем существующую функцию)
    sort_choice = get_user_choice("Отсортировать операции по дате? Да/Нет: ", ["Да", "Нет"])
    if sort_choice == "Да":
        order = get_user_choice("Отсортировать по возрастанию или по убыванию? ", ["по возрастанию", "по убыванию"])
        reverse = order == "по убыванию"
        filtered = sort_by_date(filtered, reverse=reverse)

    # Фильтр по рублёвым транзакциям
    rub_choice = get_user_choice("Выводить только рублевые транзакции? Да/Нет: ", ["Да", "Нет"])
    if rub_choice == "Да":
        # Предполагаем, что в транзакциях есть поле "currency" с вложенным "code"
        filtered = [t for t in filtered if t.get("currency", {}).get("code") == "RUB"]

    # Поиск по описанию (новая функция)
    desc_choice = get_user_choice(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ", ["Да", "Нет"]
    )
    if desc_choice == "Да":
        search_word = input("Введите слово для поиска: ").strip()
        filtered = filter_by_description(filtered, search_word)

    # Вывод результата
    print("Распечатываю итоговый список транзакций...")
    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered)}")
    # Форматированный вывод согласно примеру
    for t in filtered:
        # Пример вывода: дата, описание, счёт/карта, сумма и валюта
        # Упрощённо выводим весь словарь
        print(t)


if __name__ == "__main__":
    main()
