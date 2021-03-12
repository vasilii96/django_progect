from django.contrib import admin


from .models import *
# Register your models here.

'''
Создали суперпользлвателя для работы с админ-панелью, в файле admin.py зарегистрировали модель/и(User).
В руссифицировали админ-панель.   создали class Meta в файле models.py, которые изменилиназвание приложения на пациенты.
так же были созданы классы UserAdmin и LoginAdmin для пердставления данных в удобном виде в админ-панеле 

'''
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'second_name', 'dob')
    list_editable = ['dob']

class LoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'password')

admin.site.register(User, UserAdmin) # Регистрация базы данных класса User и преобразования к удобному виду
admin.site.register(Login, LoginAdmin) # # Регистрация базы данных класса Login и преобразования к удобному виду

