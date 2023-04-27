import json
import textwrap
from datetime import datetime


def get_json(file_path):
    """
    Принимает json файл и возвращает его содержимое.
    :param file_path: Путь к json файлу
    :return: Данные в json формате
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def sort_by_date_dictionary_list(list_name):
    # Обрабатываем список, исключая из него пустые словари без ключа 'date'
    new_list = [dictionary for dictionary in list_name if 'date' in dictionary]

    # Сортируем обработанный список
    sorted_new_list = sorted(new_list, key=lambda x: x['date'], reverse=True)

    return sorted_new_list


def get_latest_executed_transactions(list_name):
    """
    Принимает список всех операций, и возвращает список из пяти ВЫПОЛНЕННЫХ операций.
    :param list_name: Список словарей, содержащих информацию обо всех операциях.
    :return: Список словарей, состоящий из пяти выполненных операций.
    """
    latest_transactions = []

    for dictionary in list_name:
        if dictionary['state'] == 'EXECUTED':
            latest_transactions.append(dictionary)

        if len(latest_transactions) == 5:
            return latest_transactions


def mask_information(data: str):
    """
    Определяет номер карты или номер счета содержится в строке.
    Маскирует информацию и возвращает ее для дальнейшего использования.
    :param data: Строка, содержащая номер карты или номер счета.
    :return: f-строка, содержащая замаскированную информацию.
    """
    if 'счёт' in data.lower() or 'счет' in data.lower():

        return f'{data[:4]} **{data[-4:]}'

    else:
        data_list = data.split(' ')

        card_number = None

        for value in data_list:
            if value.isdigit():
                card_number = value

        split_card_number = ' '.join(textwrap.wrap(card_number, 4))

        return f'{data[:-len(card_number)]}{split_card_number[:7]}** **** {split_card_number[-4:]}'


def display_information(list_name):
    """
    Перебирает список словарей, собирая из них информацию, необходимую для вывода пользователю, и выводит ее на экран.
    :param list_name: Список словарей с информацией о транзакциях.
    """
    for dictionary in list_name:
        # Обрабатываем дату и сохраняем ее в нужном нам формате: ДД.ММ.ГГГГ
        date = datetime.strptime(dictionary['date'][0:10], "%Y-%m-%d").date().strftime("%d.%m.%Y")

        description = dictionary['description']

        if 'from' in dictionary:
            from_ = mask_information(dictionary['from'])
        else:
            from_ = 'Unknown'

        to = mask_information(dictionary['to'])

        amount = dictionary['operationAmount']['amount']

        currency = dictionary['operationAmount']['currency']['name']

        print(f'{date} {description}\n{from_} -> {to}\n{amount} {currency}\n')
