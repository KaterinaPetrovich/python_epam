# Generated by Django 4.0.1 on 2022-01-10 20:23

from django.db import migrations


def add(apps, schema_editor):
    Teacher = apps.get_model("app", "Teacher")
    Student = apps.get_model("app", "Student")
    Homework = apps.get_model("app", "Homework")
    HomeworkResult = apps.get_model("app", "HomeworkResult")

    teacher = Teacher.objects.create(first_name="Petr",
                                     last_name="Petrov")
    student = Student.objects.create(first_name="Michail",
                                     last_name="Orlov")
    hw = Homework.objects.create(text="qwerty", deadline=7, author=teacher)
    HomeworkResult.objects.create(solution="asdfg", author=student, task=hw)


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add),
    ]
