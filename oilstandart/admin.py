from django.contrib import admin
from .models import PriceAndCompany
from .models import Contacts

admin.site.register(PriceAndCompany)  #Чтобы наша модель была доступна на странице администрирования, необходимо её зарегистрировать
admin.site.register(Contacts)