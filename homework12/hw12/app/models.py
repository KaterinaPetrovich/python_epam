import datetime

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    app_label = 'app'

    def create_homework(self, text, deadline):
        return Homework.objects.create(author=self, text=text,
                                       deadline=deadline)


class Homework(models.Model):
    text = models.TextField()
    deadline = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def is_active(self):
        return (self.created + self.deadline) > datetime.datetime.now()


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult.objects.create(
                author=self, task=homework, solution=solution)
        else:
            return None


class HomeworkResult(models.Model):
    solution = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Homework, on_delete=models.CASCADE)
