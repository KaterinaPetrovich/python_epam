import pytest

from homework6.task2 import DeadlineError, Student, Teacher

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")

oop_homework = teacher.create_homework("create 2 simple classes", 5)
good_result = student.do_homework(oop_homework, "solution")
another_good_result = student.do_homework(oop_homework, "another solution")
bad_result = student.do_homework(oop_homework, "bad")
expired_homework = teacher.create_homework("expired", 0)


def test_do_homework_creation_homework_result():
    assert good_result.solution == "solution"


def test_do_expired_homework():
    with pytest.raises(DeadlineError):
        student.do_homework(expired_homework, "solution")


def test_check_homework_add_to_homework_done():
    teacher.check_homework(good_result)
    assert Teacher.homework_done.get(good_result.homework) == good_result.solution


def test_reset_results():
    teacher.check_homework(another_good_result)
    teacher.reset_results(another_good_result.homework)
    assert not Teacher.homework_done.get(another_good_result.homework)


def test_check_bad_homework_result():
    assert not teacher.check_homework(bad_result)
