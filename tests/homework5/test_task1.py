from homework5.task1 import Homework, Student, Teacher

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")
expired_homework = teacher.create_homework("Learn functions", 0)
create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)


def test_teachers_last_name():
    assert teacher.last_name == "Shadrin"


def test_students_first_name():
    assert student.first_name == "Roman"


def test_expired_homework_is_not_active():
    assert not expired_homework.is_active()


def test_homework_text():
    assert expired_homework.text == "Learn functions"


def test_do_actual_homework():
    assert student.do_homework(oop_homework) == oop_homework


def test_do_expired_homework():
    assert student.do_homework(expired_homework) is None
