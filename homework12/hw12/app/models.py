from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Homework(models.Model):
    text = models.TextField()
    deadline = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class HomeworkResult(models.Model):
    solution = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Homework, on_delete=models.CASCADE)
