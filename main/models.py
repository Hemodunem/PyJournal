from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=60, default = 'name')
    surname = models.CharField(max_length=60, default = 'surname')
    patronymic = models.CharField(max_length=60, default = 'patronymic')

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic


class Student(Person):
    year = models.IntegerField(default=1)
    pass


class Teacher(Person):
    pass


class Subject(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Mark(models.Model):
    value = models.IntegerField()
    data = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null = True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, null = True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null = True)
