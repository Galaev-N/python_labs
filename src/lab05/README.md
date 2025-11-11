<h1>Задание А<h1>

## Для выполнения задания нам понадобился ряд библиотек:
```python
from pathlib import Path
import csv
import sys
import json
sys.path.append(r'/Users/galaevka/python_labs/python_labs/src/lab04')
from io_txt_csv import *
```

## Запись данных из файла формата файла json в csv
```python
def json_to_csv(json_path, csv_path):

    if json_path[-4:] != 'json' :
         return f'TypeError! Неверный формат файла {json_path}'
    
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
    except json.decoder.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list):
        raise 'FileError'
    
    header = tuple(data[0].keys())

    rows = []
    for i in data:
        if not isinstance(i, dict):
                raise ValueError("Список с не-словарами")
        rows.append(tuple(i.values()))

    write_csv(rows, csv_path, header)
    return 'Файл успешно создан'
```

![alt text](<../../images/lab05/Снимок экрана 2025-11-11 в 13.36.34.png>)

## Запись данных из файла формата файла csv в json(функция, обратная предыдущей)
```python
def csv_to_json(csv_path, json_path):
    if csv_path[-3:] != 'csv' :
        return f'TypeError! Неверный формат файла {csv_path}'

    csv_path = Path(csv_path)
    json_path = Path(json_path)

    try:
        with open(csv_path , encoding="utf-8") as csv_file:
            data = csv.DictReader(csv_file)
            rows = list(data)
    except:
        raise FileNotFoundError("Осутствующий файл")
    
    if not rows:
        return ValueError("Пустой CSV")
    
    if not data.fieldnames:     
        return ValueError("CSV без заголовка")
    
    with open(json_path,'w', encoding="utf-8" ) as json_file:
        json.dump(rows, json_file, indent=1000)
    return 'Файл успешно создан'
```

![alt text](<../../images/lab05/Снимок экрана 2025-11-11 в 13.42.28.png>)

## После выполнения выбранной функции, на основе файла необходимого формата создается новый файл. Обе функции не требуют ввода кода запуска, их необходимо запускать в самом коде.



<h1>Задание B<h1>

## Для задания B также потребовалось несколько библиотек:
```python
from pathlib import Path
import csv
from openpyxl import Workbook
```
<p> openpyxl - библиотека используемая для удобной работы с файлами, формата xl(инициализация, создание, чтение и тд.)</p>

## Код второой задачи
```python
def csv_to_xlsx(csv_path, xlsx_path):
    if csv_path[-3:] != 'csv' :
        return f'TypeError! Неверный формат файла {csv_path}'

    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    try:
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            data = list(csv.reader(csv_file))

    except FileNotFoundError:
        raise FileNotFoundError("Осутствующий файл")
    
    if not data:
        return 'ValueError! Пустой CSV'
    
    headers = data[0]

    if not headers:
        return 'ValueError! Пустой заголовок в CSV'
    
    wb = Workbook()
    ws = wb.active
    for i in data:
        ws.append(i)
    wb.save(xlsx_path)
```
## После выполнения кода этой функции на основе данных из [*csv*](data/input) файла создается [*json*](data/output) файл, все файлы находятся в папке [*data*](python_labs-3/data).

![alt text](<../../images/lab05/Снимок экрана 2025-11-11 в 13.44.58.png>)