from pathlib import Path
import csv
from openpyxl import Workbook

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
    
csv_to_xlsx('/Users/galaevka/python_labs-3/src/lab05/B.csv', '/Users/galaevka/python_labs-3/src/lab05/B.xlsx')
