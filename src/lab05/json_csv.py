from pathlib import Path
import csv
import sys
import json

sys.path.append(r"/Users/galaevka/python_labs/python_labs/src/lab04")
from io_txt_csv import *


def json_to_csv(json_path, csv_path):

    if json_path[-4:] != "json":
        return f"TypeError! Неверный формат файла {json_path}"

    json_path = Path(json_path)
    csv_path = Path(csv_path)

    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

    except json.decoder.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list):
        raise "FileError"

    header = tuple(data[0].keys())

    rows = []
    for i in data:
        if not isinstance(i, dict):
            raise ValueError("Список с не-словарами")
        rows.append(tuple(i.values()))

    write_csv(rows, csv_path, header)
    return "Файл успешно создан"


# print(json_to_csv('data/lab05/input/first.json', 'data/lab05/output/first.csv'))


def csv_to_json(csv_path, json_path):
    if csv_path[-3:] != "csv":
        return f"TypeError! Неверный формат файла {csv_path}"

    csv_path = Path(csv_path)
    json_path = Path(json_path)

    try:
        with open(csv_path, encoding="utf-8") as csv_file:
            data = csv.DictReader(csv_file)
            rows = list(data)
    except:
        raise FileNotFoundError("Осутствующий файл")

    if not rows:
        return ValueError("Пустой CSV")

    if not data.fieldnames:
        return ValueError("CSV без заголовка")

    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(rows, json_file, indent=2)
    return "Файл успешно создан"


# print(csv_to_json('/Users/galaevka/python_labs-3/data/lab05/input/second.csv', '/Users/galaevka/python_labs-3/data/lab05/output/second.json'))
