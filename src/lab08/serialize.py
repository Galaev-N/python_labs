from models import Student
from pathlib import Path
import json


def students_to_json(students, path):
    path = Path(path)
    data = [s.to_dict() for s in students]
    json.dumps(data, ensure_ascii=False, indent=2)


def students_from_json(json_path):
    json_path = Path(json_path)
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


Person = Student("Николай", "2007-03-19", "BIVT-25-5", 3.59)
