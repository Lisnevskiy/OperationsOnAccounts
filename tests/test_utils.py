import pytest

from src.utils import get_json, sort_by_date, get_executed_transactions, mask_information, display_information

from test_data import DATA_FOR_SORT_BY_DATE, DATA_FOR_GET_EXECUTED_TRANSACTIONS, OPERATIONS_LIST, OUTPUT_INFORMATION, \
    TRANSACTIONS


def test_get_json(json_file):
    expected_data = {'key': 'value'}
    assert get_json(json_file) == expected_data


@pytest.mark.parametrize("test_input, expected", DATA_FOR_SORT_BY_DATE)
def test_sort_by_date(test_input, expected):
    assert sort_by_date(test_input) == expected


@pytest.mark.parametrize("test_input, expected", DATA_FOR_GET_EXECUTED_TRANSACTIONS)
def test_1_get_executed_transactions(test_input, expected):
    assert get_executed_transactions(test_input) == expected


def test_2_get_executed_transactions():
    result = get_executed_transactions(TRANSACTIONS)
    assert len(result) == 5
    for transaction in result:
        assert transaction['state'] == 'EXECUTED'


def test_mask_information():
    assert mask_information('Счет 96119739109420349721') == 'Счет **9721'
    assert mask_information('MasterCard 8826230888662405') == 'MasterCard 8826 23** **** 2405'


def test_display_information(capfd):
    """
    Вызываем функцию `display_information`, а затем перехватываем ее вывод с помощью `capfd.readouterr()`.
    Затем проверяем, что ожидаемая информация была выведена на экран с помощью `assert`.
    Если информация не была выведена, то тест не пройдет.
    """
    display_information(OPERATIONS_LIST)
    captured = capfd.readouterr()
    assert OUTPUT_INFORMATION in captured.out
