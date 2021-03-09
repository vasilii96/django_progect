from django.urls import path
from medsite.views import *


'''
В списке urlpatterns прописываются все маршруты текущего приложения
'''

urlpatterns = [
    path('', index), # http://127.0.0.1:8000 (Такой url)
    path('test/<slug:testid>/', test), # http://127.0.0.1:8000/medsite/test (так будет формироваться url (Пример тестового))
    path('about/', about),
    # path('login/', login, name=login), # Прописываю страницы для тестовой обработки html страниц
    # path('enter/', enter, name=enter) # Прописываю страницы для тестовой обработки html страниц

]