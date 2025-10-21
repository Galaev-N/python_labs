<h1>Задание А<h1>

## Для выполнения задания нам понадобился ряд библиотек:
```python
from pathlib import Path
import csv
import sys
sys.path.append(r'/Users/galaevka/python_labs/python_labs/src/lab03')
from A import *
```

## Чтение текста
```python
def read_text(path, encoding='utf-8'):
    p = Path(path)
    try:
        return normalize(p.read_text(encoding=encoding), True, True)
    except FileNotFoundError:
        print(f'Файл {p} не найден.')
        return ''
    except UnicodeDecodeError:
        print(f'Неверная кодировка. Должна быть {encoding}.')
        return ''

all_text = read_text('/Users/galaevka/python_labs/python_labs/src/lab04/text', 'utf-8')
```

## Создание CSV файла
```python
def write_csv(rows, path, header = None):
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f: # открываем файл для записи и запоминаем как f
        w = csv.writer(f) # обозначаем инструмент записи в файл f как w
        if header is not None:
            w.writerow(header)
        else:
            header = ('Word','count')
            w.writerow(header)
        for r in rows:
            if len(r) == 2:
                w.writerow(r)
            else:
                return 'ValueError'
        return ''
```

## Код для наполнения csv файла нужными данными
```python
all_text = read_text('/Users/galaevka/python_labs/python_labs/src/lab04/text', 'utf-8')
data = []
for i in top_n(count_freq(tokenize(all_text)), 5):
    data.append(((f'{i[0]}'),(f'{i[1]}')))
```

## По средством выполнения кода файл [text](text) в папке [lab04](/python_labs/src/lab04) читается и на его основе в этой же папке создается файл report.csv

![alt text](<../../images/lab04/Снимок экрана 2025-10-21 в 12.34.38.png>)

<h1>Задание B<h1>

## Для задания B также потребовалось несколько библиотек:
```python
import argparse
import os
from io_txt_csv import *
import sys
```

## Основной блок кода
```python
def main():
    parser = argparse.ArgumentParser(description='Обработка файлов')
    parser.add_argument('--in', dest='input_file', required=True)
    parser.add_argument('--out', dest='output_file', required=True)
    
    args = parser.parse_args()
    
    # Работа с файлами
    process_files(args.input_file, args.output_file)

def process_files(input_path, output_path):
    # Создаем папку для выходного файла, если её нет
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        all_text = read_text(input_path, encoding='utf-8')

        data = []
        for i in top_n(count_freq(tokenize(all_text)), 5):
            data.append(((f'{i[0]}'),(f'{i[1]}')))
            
        write_csv(data, output_path, ('word','count'))

        
    except FileNotFoundError:
        print(f"Файл {input_path} не найден")
        
    except Exception as e:
        print(f"Ошибка при обработке файлов: {e}")

if __name__ == "__main__":
    main()
```
## После выполнения кода текст, содержащийся в папке data будет обработан и в ней же будет создан out.csv. Если папки data и файла in.txt не существует, код выдаст ошибку, однако создаст папку и пустой csv(содержащий только 'word, count')

![alt text](<../../images/lab04/Снимок экрана 2025-10-21 в 13.15.39.png>)