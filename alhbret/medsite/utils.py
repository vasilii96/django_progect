from django.views.generic.detail import SingleObjectMixin
from django.forms import ModelForm, TextInput, Textarea, PasswordInput

from medsite.models import *

class DataMixin:
    class Meta:
        model = "#" #<------Указаваем модель с которой работаем
        fields = ['#', '#', '#'] #<-------Указываем название рабочих полей участвуевших в моделе
        widgets = {
                    'email': TextInput(attrs={
                        'class':'form-control',
                            'placeholder':'Введите Email'
                                })
}