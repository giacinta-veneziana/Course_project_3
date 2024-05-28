import json
from pathlib import Path

def load_json(path: Path) -> list[dict]:
    """
    Функция для чтения .json файла
    :принимает на вход: путь до файла
    :возвращает: список словарей
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)