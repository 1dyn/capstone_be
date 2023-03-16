from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()

class Scholarship(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    personnel_num = models.CharField(max_length=50)
    benefit = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    view_num = models.IntegerField()