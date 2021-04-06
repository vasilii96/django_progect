from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# from medsite.forms import Loginform

# from django.contrib.auth.decorators import LoginRequired

from medsite.views import *
from .models import *
from .forms import *
from .models import Login
from .models import User
import sqlite3

'''Функции представления страниц '''

menu = [{'title': 'О сайте', 'url_name':'about'},
        {'title': 'Регистрация', 'url_name': 'login'},
        {'title': 'Войти', 'url_name': 'enter'}        # О сайте', 'Регистрация', 'Войти'
]


# def add_user(request):
#     form = AddUserForm()
#     return render(request, 'medsite/adduser.html')
    

def index(request):  # Гравная, 3й параметр получает словаль, для использавание его в шаблонах html страниц
    users = User.objects.all()
    # SELECT "medsite_user"."name"
    # FROM "medsite_user"
    # users_sum = len(users)
    # conn = sqlite3.connect('D:\\Python\\work_vasilii\\django_progect\\alhbret\\db.sqlite3') # подключаемся к базе данных
    # cur = conn.cursor() #осле создания объекта соединения с базой данных нужно создать объект cursor. Он позволяет делать SQL-запросы к базе
    # cur.execute("SELECT name FROM medsite_user")
    # user_name= cur.fetchall()
    # conn.commit()
    # conn.close()
    return render(request, 'medsite/index.html', {'users': users, 'title' : 'Главная страница', 'menu': menu} )



def about(request): # Тестовая страница о Нас
    return render(request,'medsite/about.html',{'title' : 'Страница о нас', 'menu': menu})



def index2(request): #<-----Создана для проверки формы Login
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'форма не корректная'

    form = LoginForm()
    context = {
        'form':form
        # 'error':error

    }
    return render(request,'medsite/index2.html', context)



def form_pac(request): #<-----Создана для проверки формы User
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'форма не корректная'

    form = UserForm()
    context = {
        'form':form
        # 'error':error

    }
    return render(request,'medsite/form_pac.html', context)


'''
Тестовая часть для формы работы с базой данных
'''

def injection():
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'форма не корректная'

    form = UserForm()
    context = {
        'form': form
        # 'error':error

    }
    pass



def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')



## def enter(request): # Тестовая страница Вход
#     return HttpResponse('Вход')

def test(request, testid): # Тестовая проверочная страница
    if (request.POST):
        print(request.POST)
    return HttpResponse(f'<h1>Test page<h1> <p>{testid}</p>') # Формирование url следующим образом http://127.0.0.1:8000/test/1/

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<\h1>')


