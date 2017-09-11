from django.db import models
from django.utils import timezone


class Price(models.Model):
    author = models.ForeignKey('auth.User') #Ссылка на другую модель
    price = models.CharField(max_length=200)#Ограничение числовых символов
    created_date = models.DateTimeField(
            default=timezone.now)  #Дата и время
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):    
        self.published_date = timezone.now()
        self.save()   #Метод публикации нашей записи

    def __str__(self): 
        return self.price  #Этот метод возвращает что-то. В данном случае title

