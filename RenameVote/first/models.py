from django.db import models

# Create your models here.


class CalcHistory(models.Model):
    date = models.DateTimeField()
    first = models.IntegerField()
    second = models.IntegerField()
    result = models.IntegerField()