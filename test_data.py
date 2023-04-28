DATA_FOR_SORT_BY_DATE = [([], []),
                         ([{"date": "2018-09-27T14:26:24.629306"}],
                          [{"date": "2018-09-27T14:26:24.629306"}]),
                         ([{'date': '2022-01-01'}, {'date': '2021-12-31'}, {'date': '2022-01-02'}],
                          [{'date': '2022-01-02'}, {'date': '2022-01-01'}, {'date': '2021-12-31'}])
                         ]

DATA_FOR_GET_EXECUTED_TRANSACTIONS = [([], []),
                                      ([{"state": "EXECUTED"}], [{"state": "EXECUTED"}]),
                                      ([{"state": "EXECUTED"}, {"state": "CANCELED"}], [{"state": "EXECUTED"}])]

TRANSACTIONS = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'CANCELED'},
    {'id': 3, 'state': 'EXECUTED'},
    {'id': 4, 'state': 'EXECUTED'},
    {'id': 5, 'state': 'CANCELED'},
    {'id': 6, 'state': 'EXECUTED'},
    {'id': 7, 'state': 'EXECUTED'},
    {'id': 8, 'state': 'EXECUTED'},
]

OPERATIONS_LIST = [
    {
        "id": 86608620,
        "state": "EXECUTED",
        "date": "2019-08-16T04:23:41.621065",
        "operationAmount": {
            "amount": "6004.00",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "MasterCard 8826230888662405",
        "to": "Счет 96119739109420349721"
    },
    {
        "id": 86608620,
        "state": "EXECUTED",
        "date": "2019-08-16T04:23:41.621065",
        "operationAmount": {
            "amount": "6004.00",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "to": "Счет 96119739109420349721"
    }
]

OUTPUT_INFORMATION = '16.08.2019 Перевод с карты на счет\n' \
                     'MasterCard 8826 23** **** 2405 -> Счет **9721\n' \
                     '6004.00 руб.\n\n' \
                     '16.08.2019 Перевод с карты на счет\n' \
                     'Unknown -> Счет **9721\n' \
                     '6004.00 руб.\n\n'
