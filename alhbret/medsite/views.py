from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from medsite.views import *
from .models import *

'''Функции представления страниц '''

menu = [{'title': 'О сайте', 'url_name':'about'},
        {'title': 'Регистрация', 'url_name': 'login'},
        {'title': 'Войти', 'url_name': 'enter'}
        # О сайте', 'Регистрация', 'Войти'
         ]


def index(request):  # Гравная, 3й параметр получает словаль, для использавание его в шаблонах html страниц
    users = User.objects.all()
    return render(request, 'medsite/index.html', {'users': users, 'title' : 'Главная страница', 'menu': menu} )

def about(request): # Тестовая страница о Нас
    return render(request,'medsite/about.html',{'title' : 'Страница о нас', 'menu': menu})

# def login(request): # Тестовая страница login
#     return HttpResponse('Регистрация')
#
# def enter(request): # Тестовая страница Вход
#     return HttpResponse('Вход')

def test(request, testid): # Тестовая проверочная страница
    if (request.POST):
        print(request.POST)
    return HttpResponse(f'<h1>Test page<h1> <p>{testid}</p>') # Формирование url следующим образом http://127.0.0.1:8000/test/1/

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<\h1>')


