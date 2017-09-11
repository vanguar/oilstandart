from django.contrib import admin
from .models import Price #Импортировали модель Post

admin.site.register(Price)  #Чтобы наша модель была доступна на странице администрирования, необходимо её зарегистрировать
