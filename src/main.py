from src.utils import get_json, get_executed_transactions, sort_by_date, display_information

PATH_TO_JSON = '../data/operations.json'


def main():
    # Получаем отсортированный по датам список операций.
    operations_list = sort_by_date(get_json(PATH_TO_JSON))

    # Получаем список пяти последних выполненных операций.
    latest_transactions = get_executed_transactions(operations_list)

    # Выводим полученную информацию в необходимом формате на экран.
    display_information(latest_transactions)


if __name__ == '__main__':
    main()
