from django import forms
from .models import *

'''Создадим форму добавления пациента в базу данных'''
#
# class AddUserForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     second_name = forms.CharField(max_length=255)
#     middle_name = forms.CharField(max_length=255)
#     dob = forms.CharField(max_length=100)
#     slug = forms.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
