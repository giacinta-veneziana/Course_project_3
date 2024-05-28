from pytest import *
from src.utils import *
from src.classes import *

op1 =   {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
  }

op2 = {
    "id": 716496732,
    "state": "CANCELLED",
    "date": "2018-04-04T17:33:34.701093",
    "operationAmount": {
      "amount": "40701.91",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 5999414228426353",
    "to": "Счет 72731966109147704472"
  }

op3 = {}
def test_get_operations_list():
    op_list = get_operations_list([op1, op2, op3])
    assert op_list[0].pk == op1["id"]
    assert op_list[0].state == op1["state"]
    assert op_list[0].description == op1["description"]
    assert op_list[1].pk == op2["id"]
    assert op_list[1].state == op2["state"]
    assert op_list[1].description == op2["description"]
    assert op_list[2].pk == None
    assert op_list[2].state == None
    assert op_list[2].description == None


def test_sort_executed_operations():
    op_list = [Operation(op1), Operation(op2), Operation(op3)]
    assert sort_executed_operations(op_list) == op_list[:1]


def test_format_account():
    assert format_account("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"
    assert format_account(None) == ""
    assert format_account("Счет 72731966109147704472") == "Счет  **4472"
    assert format_account("Maestro 3928549031574026") == "Maestro 3928 54** **** 4026"

def test_format_output():
    op = Operation(op1)
    assert format_output(op) == "19.08.2018 Перевод с карты на карту\nVisa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229\n56883.54 USD\n"
    op = Operation(op2)
    assert format_output(op) == "04.04.2018 Перевод организации\nVisa Gold 5999 41** **** 6353 -> Счет  **4472\n40701.91 USD\n"