import json
from pathlib import Path
from src.classes import Operation
from settings import *

def load_json(path: Path) -> list[dict]:
    """
    Функция для чтения json-файла, принимает на вход: путь до файла, возвращает: список словарей
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_operations_list(records: list[dict]) -> list:
    """
    Получает на вход список словарей, преобразовывает его в список объектов класса Operation
    """
    operations_list = [Operation(record) for record in records]
    return operations_list


def sort_executed_operations(operation_list: list[Operation]) -> list:
    """
    Функция принимает список всех объектов класса Operation и возвращает только список выполненных операций
    """
    executed_operations = [operation for operation in operation_list if operation.state == "EXECUTED"]
    return sorted(executed_operations, key=lambda x: x.date, reverse=True)


def format_account(account):
    """
    Функция принимает номер счета или карты и выводит его в необходимом формате
    """
    if account == None:
        return ""
    account_type = [char for char in account if not char.isdigit()]
    account_type = "".join(account_type)
    account_number = [char for char in account if char.isdigit()]
    account_number = "".join(account_number)
    if account_type.strip() == "Счет":
        return f"{account_type} **{account_number[-4:]}"
    return f"{account_type}{account_number[0:4]} {account_number[4:6]}** **** {account_number[-4:]}"


def format_output(operation: Operation) -> str:
    """
    Функция принимает объект класса "Operation", а выводит строку в необходимом формате
    """
    return (f"{operation.date.strftime('%d.%m.%Y')} {operation.description}\n"
            f"{format_account(operation._from)} -> {format_account(operation.to)}\n"
            f"{operation.amount} {operation.currency}\n")

