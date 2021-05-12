from django import forms
from django.forms import ModelForm, TextInput, Textarea, PasswordInput
from django.contrib.auth.forms import *
from django.contrib.auth import get_user_model
# from auth.models import User
from django.contrib.auth.models import *
from .utils import *
from .models import *
# from .forms import LoginForm


'''Создадим функционал для работы html формы Регистрации'''

class LoginForm(ModelForm):
    class Meta:
        model = Login #<------Указаваем модель с которой работаем
        fields = ['email', 'password', 'password2'] #<-------Указываем название рабочих полей участвуевших в моделе
        widgets = {
                    'email': TextInput(attrs={
                        'class':'form-control',
                            'placeholder':'Введите Email'
                                }),
                    'password': TextInput(attrs={
                        'class': 'form-control',
                            'placeholder':'Введите пароль'
                                }),
                    'password2': TextInput(attrs={
                        'class': 'form-control',
                            'placeholder':'Повторите пароль'
        }),
        }

'''
Создадим функционал для работы html формы данных о пользователях.
'''


class UserForm(ModelForm):
    class Meta:
        model = User #<--------Указываем модель с которой работаем
        fields = ['name', 'second_name', 'middle_name','dob'] # <----Указываем названия полей в моделе
        widgets = {
            'name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите имя'
            }),
            'second_name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите фамилию'
            }),
            'maiddle_name': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите отчество'
            }),
            'dob': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения'
            }),
            'mail_id': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите id'

            })
        }
'''
Пробный класс
'''

# class MyForm(forms.Form):
#     CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
#     field = forms.ChoiceField(choices=CHOICES)
#
# print (MyForm().as_p())

