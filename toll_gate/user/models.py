# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#
# class Person(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     birthdate = models.DateField(null=True, blank=True)
#     vehicle_number = models.CharField(max_length=11)
#     sex = models.CharField(max_length)
#
#     def __str__(self):
#         return self.name+self.vehicle_number

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True, blank=True)
    vehicle_number = models.CharField(max_length=11)
    sex = models.CharField(max_length=1)
    money = models.FloatField(default=0)
    def __str__(self):
        return self.user.useran