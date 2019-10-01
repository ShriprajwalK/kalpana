from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
#
# class PersonForm(forms.ModelForm):
#     name = forms.CharField(label='Your name')
#     vehicle_number_plate = forms.CharField(label='Your vehicle number')
#     MALE = 'M'
#     FEMALE = 'F'
#
#     GENDER_CHOICES = [
#         (MALE, 'Male'),
#         (FEMALE, 'Female'),
#     ]
#     sex = models.CharField(
#         max_length=1,
#         choices=GENDER_CHOICES,
#         default=MALE,
#     )
#
#
#     class Meta:
#
