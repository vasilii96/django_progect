from django.urls import path
from medsite.views import *


'''
В списке urlpatterns прописываются все маршруты текущего приложения
'''

urlpatterns = [
    path('', index), # http://127.0.0.1:8000/medsite/ (Такой url)
    path('test/', test), # http://127.0.0.1:8000/medsite/test (так будет формироваться url (Пример тестового))
]