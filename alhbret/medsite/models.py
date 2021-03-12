from django.db import models

'''Работа с базами данных(модели), описание работы с моделями '''

class User(models.Model):
    # id поле автоматически устанавливается в джанго
    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    dob = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL') # надо сделать миграции
    mail_id = models.ForeignKey('Login', on_delete = models.PROTECT, null=True) # Сщздали ключ для связи таблиц, без возможности
                                                                                # удаления записи из другой таблицы
    def __str__(self):
        return self.name
    # pass
    '''Преобразование  админ-понели джанго'''

    class Meta:
        verbose_name = 'Пациенты'
        verbose_name_plural = 'Пациенты'
        ordering = ['name'] # Сортировка в базе данных через админ панель

class Login(models.Model):
    # Надо ли здесь устанавливать  id???
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)    # pass
    password2 = models.CharField(max_length=255)
    def __str__(self):
        return self.email
# class Configurator(models.Model):
#     pass

    class Meta:
        verbose_name = 'Данные пациентов'
        verbose_name_plural = 'данные пациентов'

