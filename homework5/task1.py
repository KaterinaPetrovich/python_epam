import datetime


class Homework:
    def __init__(self, text: str, days: int):
        self.text = text
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return datetime.datetime.now() - self.created < self.deadline


class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, hw: Homework) -> Homework:
        if hw.is_active():
            return hw
        else:
            print("you are late")
            return None


class Teacher:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text: str, days: int) -> Homework:
        return Homework(text, days)
