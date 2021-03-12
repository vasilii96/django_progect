from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea

'''Создадим форму добавления пациента в базу данных'''
#
# class AddUserForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     second_name = forms.CharField(max_length=255)
#     middle_name = forms.CharField(max_length=255)
#     dob = forms.CharField(max_length=100)
#     slug = forms.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


'''Создадим функционал для работы html формы Регистрации'''

class LoginForm(ModelForm):
    class Meta:
        model = Login #<------Указаваем модель с которой работаем
        fields = ['email', 'password', 'password2'] #<-------Указываем название рабочих полей участвуевших в моделе
        widgets = {
                    'email': TextInput(attrs=={
                        'class':'form-control'
                            'placeholder':'Введите Email'
                                }),
                    'password': TextInput(attrs=={
                        'class': 'form-control'
                            'placeholder':'Введите пароль'
                                }),
                    'password2': TextInput(attrs=={
                        'class': 'form-control'
                            'placeholder':'Повторите пароль'
        })
        }