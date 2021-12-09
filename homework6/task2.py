import datetime
from collections import defaultdict


class Homework:
    def __init__(self, text: str, days: int):
        self.text = text
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return datetime.datetime.now() - self.created < self.deadline


class Human:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(Human):
    def do_homework(self, hw: Homework, solution: str):
        if hw.is_active():
            return HomeworkResult(hw, solution, self)
        else:
            raise DeadlineError


class HomeworkResult:
    def __init__(self, homework: Homework, solution, author: Student):
        if not isinstance(homework, Homework):
            raise ValueError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Teacher(Human):
    homework_done = defaultdict(set)

    def create_homework(self, text: str, days: int) -> Homework:
        return Homework(text, days)

    def check_homework(self, hw_result: HomeworkResult) -> bool:
        if not len(hw_result.solution) > 5:
            return False
        else:
            Teacher.homework_done[hw_result.homework] = hw_result.solution
            return True

    def reset_results(self, hw=None):
        if hw:
            del Teacher.homework_done[hw]
        else:
            Teacher.homework_done.clear()


class DeadlineError(Exception):
    def __init__(self):
        self.message = "You are late"
        super().__init__(self.message)
