from django.db import models
from django.utils import timezone


class PriceAndCompany(models.Model):
    author = models.ForeignKey('auth.User') #Ссылка на другую модель
    price = models.CharField(verbose_name='Цена за 1 литр', max_length=200)#Ограничение числовых символов
    company = models.CharField(verbose_name='Название компании', max_length=200)
    created_date = models.DateTimeField(verbose_name='Дата',
            default=timezone.now)  #Дата и время
    published_date = models.DateTimeField(verbose_name='Публикация даты',
            blank=True, null=True)

    class Meta:
        verbose_name_plural = "Цена продукта и название компании"

    def publish(self):    
        self.published_date = timezone.now()
        self.save()   #Метод публикации нашей записи

    
    def __str__(self): 
        return self.price  #Этот метод возвращает что-то. В данном случае price


class Contacts(models.Model):
    address = models.CharField(verbose_name='Адрес(обязательное поле)', max_length=200)
    phone_1 = models.CharField(verbose_name='Телефон №1(обязательное поле)', max_length=200)
    phone_2 = models.CharField(verbose_name='Телефон №2(необязательное поле)', blank=True, null=True, default=None, max_length=200)
    phone_3 = models.CharField(verbose_name='Телефон №3(необязательное поле)', blank=True, null=True, default=None, max_length=200)
    mail_1 = models.CharField(verbose_name='email №1(обязательное поле)', null=True, blank=True, max_length=200)
    mail_2 = models.CharField(verbose_name='email №2(необязательное поле)', null=True, blank=True, max_length=200)
    mail_3 = models.CharField(verbose_name='email №3(необязательное поле)', blank=True, null=True, max_length=200)
    Working_hours = models.CharField(verbose_name='Время работы(обязательное поле)', max_length=200)

    class Meta:
        verbose_name_plural = "Контакты"

    def __str__(self): 
        return self.address    