from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django import forms
from django.http import Http404

company_name = "«oilstandart»"


def indexoil(reguest):
    return render(reguest, 'oilstandart/indexoil.html', {'company_name': company_name})
	
def benefits(reguest): 
    return render(reguest, 'oilstandart/benefits.html', {'company_name': company_name})

def fonnumber(reguest): 
    return render(reguest, 'oilstandart/fonnumber.html')

def history(reguest): 
    return render(reguest, 'oilstandart/history.html', {'company_name': company_name})

def kerosene_0(reguest): 
    return render(reguest, 'oilstandart/kerosene_0.html')

def kerosene_1(reguest): 
    return render(reguest, 'oilstandart/kerosene_1.html')	

def petrol_0(reguest): 
    return render(reguest, 'oilstandart/petrol_0.html')

def petrol_1(reguest): 
    return render(reguest, 'oilstandart/petrol_1.html')	

def reviews(reguest):
    return render(reguest, 'oilstandart/reviews.html', {'company_name': company_name})

def smt_0(reguest): 
    return render(reguest, 'oilstandart/smt_0.html')

def smt_1(reguest): 
    return render(reguest, 'oilstandart/smt_1.html')	

def summer_0(reguest): 
    return render(reguest, 'oilstandart/summer_0.html')

def summer_1(reguest): 
    return render(reguest, 'oilstandart/summer_1.html')	

def winter_0(reguest): 
    return render(reguest, 'oilstandart/winter_0.html')

def winter_1(reguest): 
    return render(reguest, 'oilstandart/winter_1.html')

def winter_2(reguest): 
    return render(reguest, 'oilstandart/winter_2.html')

def winter_3(reguest): 
    return render(reguest, 'oilstandart/winter_3.html')	
	
def saleoffuel(reguest): 
    return render(reguest, 'oilstandart/saleoffuel.html')
	
def transportationoffuel(reguest): 
    return render(reguest, 'oilstandart/transportationoffuel.html')

def fuelpumping(reguest): 
    return render(reguest, 'oilstandart/fuelpumping.html')

def fuelutilization(reguest): 
    return render(reguest, 'oilstandart/fuelutilization.html')

def rentofcontainers(reguest): 
    return render(reguest, 'oilstandart/rentofcontainers.html')

def gasolinetankerrental(reguest): 
    return render(reguest, 'oilstandart/gasolinetankerrental.html')

def miniazs(reguest): 
    return render(reguest, 'oilstandart/miniazs.html')

def oilstoragedepot(reguest): 
    return render(reguest, 'oilstandart/oilstoragedepot.html')

def cooperation(reguest): 
    return render(reguest, 'oilstandart/cooperation.html')

def queandanswers(reguest): 
    return render(reguest, 'oilstandart/queandanswers.html')

def contacts(reguest): 
    return render(reguest, 'oilstandart/contacts.html')

def qualitypassportdt(reguest): 
    return render(reguest, 'oilstandart/qualitypassportdt.html')

def qualitypassportai(reguest): 
    return render(reguest, 'oilstandart/qualitypassportai.html')


#Контактная форма для отправки сообщения		
class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))#Заполняем в скобках, чтобы тема работала в бутрстраповских стилях
	subject1 = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
	subject2 = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
	sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))#Заполняем в скобках, чтобы тема работала в бутрстраповских стилях
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))#Заполняем в скобках, чтобы тема работала в бутрстраповских стилях
	copy = forms.BooleanField(required = False)

	
def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			subject1 = form.cleaned_data['subject1']
			subject2 = form.cleaned_data['subject2']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']
            
			recipients = ['vanguar@ukr.net']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recipients.append(sender)
			try:
				send_mail([subject, subject1, subject2], message, 'vanguar@ukr.net', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'oilstandart/thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'oilstandart/contactView.html', {'form': form})
	
def thanks(reguest): # Страница вывода сообщения об отправке сообщения
    thanks = 'thanks'
    return render(reguest, 'oilstandart/thanks.html', {'thanks': thanks})		

	