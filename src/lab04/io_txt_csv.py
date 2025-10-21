from pathlib import Path
import csv
import sys
sys.path.append(r'/Users/galaevka/python_labs/python_labs/src/lab03')
from A import *


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


data = []
for i in top_n(count_freq(tokenize(all_text)), 5):
    data.append(((f'{i[0]}'),(f'{i[1]}')))

#print(data)
    
#print(write_csv(data, '/Users/galaevka/python_labs/python_labs/src/lab04/report.csv', ('word','count')))
