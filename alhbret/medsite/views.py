from django.http import HttpResponse
from django.shortcuts import render

'''Функции представления страниц '''

def index(request):  # Гравная
    return HttpResponse('Страница приложения medsite')

def test(request): # Тестовая проверочная страница
    return HttpResponse('<h1>Test_page<h1>')
