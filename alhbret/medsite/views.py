from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

'''Функции представления страниц '''

def index(request):  # Гравная
    return HttpResponse('Страница приложения medsite')

def test(request, testid): # Тестовая проверочная страница
    if (request.POST):
        print(request.POST)
    return HttpResponse(f'<h1>Test page<h1> <p>{testid}</p>') # Формирование url следующим образом http://127.0.0.1:8000/test/1/

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<\h1>')


