from pathlib import Path
from typing import Iterable, Sequence
import csv


def normalize(text, casefold, yo2e):
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')

    if casefold:
        text = text.casefold()

    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('\r', ' ')

    text_lst = text.split()

    normalize_text = ''
    for i in text_lst:
        normalize_text += i + ' '

    return normalize_text.strip()


def tokenize(text):
    base = text.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace(':', ' ').replace(';', ' ').replace('?', '')
    base = base.split()
    ans = []

    for i in base:
        if i[0].isdigit() == 0 and i[0].isalpha() == 0: pass
        else:
            ans.append(i)
    return ans


def count_freq(lst):
    ans_items = []
    ans_keys = []
    ans = {}

    for i in lst:
        if i in ans_items: pass
        else: ans_items.append(i)

    for j in ans_items:
        ans_keys.append(lst.count(j))
    
    for k in range(len(ans_keys)):
        ans.update({ans_items[k] : ans_keys[k]})

    return ans


def top_n(dict, n):
    ans = sorted(list(dict.items()), key=lambda x: (-x[1], x[0]))
    '''
    dict.items() дает близкий к необходимому формат данных, поэтому мы все еще вынуждены обернуть его в list
    key = lambda x:... позволяет соритировать список подсписков по определнным элементам подсписка
    x: (-x[1], x[0]) означаент, что сортироваться список будет по 2 "параметрам", в первую очередь сортировка
    будет учитывать 2 элемент подсписка (то есть частоту), - перед указанием параметра означает, что сортировка
    будет идти по убыванию, в то время как для 1 элемента (самого символа) все будет идти в порядке возрастания
    '''
    return ans[:n]




def read_text(path, encoding):
    p = Path(path)
    #FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    for i in p.read_text(encoding=encoding):
        if i.isdigit() == 0 and i not in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю':
            return UnicodeDecodeError
    return normalize(p.read_text(encoding=encoding), True, True)

all_text = read_text('/Users/galaevka/python_labs/python_labs/src/lab04/text', 'cp1251')



def write_csv(rows, path, header = None):
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
    return ''

data = [('word', 'count')]
for i in top_n(count_freq(tokenize(all_text)), 5):
    data.append(((f'{i[0]}'),(f'{i[1]}')))
print(write_csv(data, '/Users/galaevka/python_labs/python_labs/src/lab04/report.csv'))

print(f'Всего слов: {len(tokenize(all_text))}')
print(f'Уникальных слов: {len(set(tokenize(all_text)))}')
print('Top-5:')
for i in top_n(count_freq(tokenize(all_text)), 5):
    print(f'{i[0]}:{i[1]}')