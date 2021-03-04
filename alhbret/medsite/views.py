from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

'''Функции представления страниц '''

menu = ['О сайте', 'Регистрация', 'Войти']

def index(request):  # Гравная, 3й параметр получает словаль, для использавание его в шаблонах html страниц
    return render(request, 'medsite/index.html', {'title' : 'Главная страница', 'menu': menu} )

def about(request): # Тестовая страница о Нас
    return render(request,'medsite/about.html',{'title' : 'Страница о нас', 'menu': menu})


def test(request, testid): # Тестовая проверочная страница
    if (request.POST):
        print(request.POST)
    return HttpResponse(f'<h1>Test page<h1> <p>{testid}</p>') # Формирование url следующим образом http://127.0.0.1:8000/test/1/

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<\h1>')


