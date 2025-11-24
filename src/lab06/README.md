<h1>Задание А<h1>

## Необходимые библиотеки
```python
import argparse
import sys
from pathlib import Path
sys.path.append(r'/Users/galaevka/python_labs-3/src/lab04')
from io_txt_csv import *
sys.path.append(r'/Users/galaevka/python_labs-3/src/lab03')
from A import *
```

## Функция cat (вывод содержимого файла построчно с нумерацией при -n)
```python
def cat(file_path, count=False):
    number = 1
    try:
        with open(file_path, encoding='utf-8') as f:
            for i in f:
                if count:
                    print(f'{number}. {i.strip()}')
                else:
                    print(i.strip())
                number += 1
    except FileNotFoundError:
        return f'Ошибка. файл {file_path} не найден!'
```

## Функция stats (анализ частот слов в тексте)
```python
def stats(file_path, top=5):
    file_path = Path(file_path)
    try:
        txt = read_text(file_path)
        print(f'Всего слов: {len(tokenize(txt))}')
        print(f'Уникальных слов: {len(set(tokenize(txt)))}')
        print('Top-5:')
        for i in top_n(count_freq(tokenize(txt)), top):
            print(f'{i[0]}:{i[1]}')
    except FileNotFoundError:
        return f'Ошибка. файл {file_path} не найден!'
```

## Функция main ?инициализация? функции
```python
def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла") # Пользуемся не стандартным --in, поэтому до этого сделали subpars cat
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", dest='count', action="store_true", help="Нумеровать строки") # action - если дан аргумент -n, значит нумерация строк будет, иначе False

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()
    if args.command == "cat":
        cat(args.input, args.count)

    elif args.command == "stats":
        stats(args.input, args.top)

if __name__ == '__main__':
    main()
```

<h1>Задание B<h1>

## Рабочие библиотеки
```python
import argparse
import sys
sys.path.append(r'/Users/galaevka/python_labs-3/src/lab05')
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx
```
<p>Функции полностью взяты из lab05, их содержимое можноипосмотреть в README соответственнно 5 лабы</p>

## Функция main и ?инициализация? функции
```python
def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.out)

    elif args.command == "scv2json":
        csv_to_json(args.input, args.out)

    elif args.commnd == 'csv2xlsx':
        csv_to_xlsx(args.input, args.out)

if __name__ == '__main__':
    main()
```