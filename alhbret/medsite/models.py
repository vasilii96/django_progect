from django.db import models

'''Работа с базами данных(модели), описание работы с моделями '''

class User(models.Model):
    # id поле автоматически устанавливается в джанго
    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    dob = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # pass

class Login(models.Model):
    # Надо ли здесь устанавливать  id???
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    # pass

# class Configurator(models.Model):

#     pass



