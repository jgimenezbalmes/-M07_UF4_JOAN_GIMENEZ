from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    grau = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.CharField(max_length=20)
    phone = models.IntegerField()



class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    grau = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.CharField(max_length=20)
    phone = models.IntegerField()