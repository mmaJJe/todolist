from django.db import models
from django.contrib.auth.models import User

class Number(models.Model):
    applynumber = models.CharField(max_length=4)

class Rank(models.Model):
    number = models.ForeignKey(Number, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class EnrollTime(models.Model):
    EnrollTime = models.DateTimeField()