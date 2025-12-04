from pathlib import Path
import csv
import sys
import json

sys.path.append(r"/Users/galaevka/python_labs/python_labs/src/lab04")
from io_txt_csv import *


def json_to_csv(json_path, csv_path):

    if json_path[-4:] != "json":
        raise ValueError(f"Неверный тип файла {json_path}")

    json_path = Path(json_path)
    csv_path = Path(csv_path)

    try:
        with open(json_path, encoding="utf-8") as json_file:
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
    return ""


# print(json_to_csv('data/lab05/input/first.json', 'data/lab05/output/first.csv'))


def csv_to_json(csv_path, json_path):
    if csv_path[-3:] != "csv":
        raise ValueError(f"Неверный тип файла {csv_path}")

    csv_path = Path(csv_path)
    json_path = Path(json_path)

    try:
        with open(csv_path, encoding="utf-8") as csv_file:
            data = csv.DictReader(csv_file)
            rows = list(data)
    except:
        raise FileNotFoundError("Осутствующий файл")

    if not rows:
        raise ValueError("Пустой CSV")

    if not data.fieldnames:
        raise ValueError("CSV без заголовка")

    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(rows, json_file, indent=2)
    return ''


def main():
    json_to_csv(
        "data/lab05/input/first.json", "data/lab05/output/first.csv"
    )  # относительной путь онтосительно этого файла
    csv_to_json("data/lab05/input/people.csv", "data/lab05/output/people.json")


if __name__ == "__main__":
    main()
