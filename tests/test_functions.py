from functions import sort_of_transactions
from functions import load_transactions
from functions import check_key_is_exist
from functions import make_up_string
from functions import make_up_data_to_print
import pytest

test_dict_with_empty = [{"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
             {},
             {"state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
             {"state": "EXECUTED", "date": "2018-03-23T10:45:06.972075"}]

test_dict_item = {"id": 207126257,
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "92688.46",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "from": "Maestro 1308795367077170",
    "to": "Счет 35737585785074382265"
}

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_transactions('file')

def test_sort_of_transactions_empty():
    assert sort_of_transactions({}) == []

def test_sort_of_transactions_right():
    assert sort_of_transactions(test_dict_with_empty) == [{"state": "EXECUTED", "date": "2018-03-23T10:45:06.972075"},
                                            {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]

def test_key_is_not_exist():
    assert check_key_is_exist(test_dict_item, 'state') == False

def test_make_up_string():
    assert make_up_string(test_dict_item, 'to') == 'Счет **2265'
    assert make_up_string(test_dict_item, 'from') == 'Maestro 1308 79** **** 7170'

def test_make_up_data_to_print():
    assert make_up_data_to_print(test_dict_item) == ('13.07.2019 Открытие вклада',
                                                     'Maestro 1308 79** **** 7170 -> Счет **2265',
                                                     '92688.46 USD')