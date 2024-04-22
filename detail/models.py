from django.db import models

# Create your models here.

class Detail(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    standard = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)


