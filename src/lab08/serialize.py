from models import Student
from pathlib import Path
import json


def students_to_json(students, path):
    path = Path(path)
    data = [s.to_dict() for s in students]
    if not data:
        raise ValueError("Пустой студент :D")
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    return 'Файл успешно создан'

def students_from_json(json_path):
    ans = []
    if json_path[-4:] != "json":
        raise ValueError(f"Неверный тип файла {json_path}")
    

    json_path = Path(json_path)
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        for std in data:
            std = Student.from_dict(std)
            ans.append(std)
            
    except json.decoder.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    return ans


I = Student("Николай", "2007-03-19", "BIVT-25-5", 3.59)
HE = Student('Мишаня', '2008-05-15', 'BIVT-25-5', 3.52)
SHE = Student('Кристинка', '2008-06-19', 'BIVT-25-5', 5.00)

stds = [I, HE, SHE]
#print(students_to_json(stds, '/Users/galaevka/python_labs-3/data/lab08/students_input.json'))
print(students_from_json('/Users/galaevka/python_labs-3/data/lab08/students_input.json'))