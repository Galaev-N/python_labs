from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:  # Объявляем класс, благодаря dataclasses удобно объявляем параметры
    fio: str
    birthdate: str  # формат YYYY-MM-DD
    group: str
    gpa: float

    def __post_init__(self):  # Именно __post_init__, потому что параметры уже указаны
        try:
            datetime.strptime(
                self.birthdate, "%Y-%m-%d"
            )  # Пытаемся привести к формату YYYY-MM-DD
        except ValueError:
            raise ValueError(
                f"Неверный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD"
            )

        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA должен быть в диапазоне от 0 до 5")

    def age(self):  # Обрабатываем данные о возрасте в нужном формате
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()

        age = today.year - birth_date.year

        # Проверяем, был ли уже день рождения в этом году
        if today.month < birth_date.month or (
            today.month == birth_date.month and today.day < birth_date.day
        ):
            age -= 1

        return age

    def to_dict(self):  # Функция создания словаря из данных о студенте
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d):  # Функция создания экземпляра класса из словаря d

        # Проверяем наличие всех обязательных полей
        if len(d) != 4:
            raise ValueError(
                "Введено некорректное кол-во данных для созданя экземпляра класса!"
            )

        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):  # Функция вывода инфы в одну строку
        return f"{self.fio}, {self.group}, GPA: {self.gpa}"

    def detailed_info(self):  # Функция вывода подробной инфы
        return (
            f"Студент: {self.fio}\n"
            f"Группа: {self.group}\n"
            f"Дата рождения: {self.birthdate} (возраст: {self.age()} лет)\n"
            f"GPA: {self.gpa}"
        )
