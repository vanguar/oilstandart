from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^benefits/$', views.benefits, name='benefits'),
	# url(r'^fonnumber/$', views.fonnumber, name='fonnumber'),
	# url(r'^history/$', views.history, name='history'),
	# url(r'^kerosene_0/$', views.kerosene_0, name='kerosene_0'),
	# url(r'^kerosene_1/$', views.kerosene_1, name='kerosene_1'),
	# url(r'^petrol_0/$', views.petrol_0, name='petrol_0'),
	# url(r'^petrol_1/$', views.petrol_1, name='petrol_1'),
	# url(r'^reviews/$', views.reviews, name='reviews'),
	# url(r'^smt_0/$', views.smt_0, name='smt_0'),
	# url(r'^smt_1/$', views.smt_1, name='smt_1'),
	# url(r'^summer_0/$', views.summer_0, name='summer_0'),
	# url(r'^summer_1/$', views.summer_1, name='summer_1'),
	# url(r'^winter_0/$', views.winter_0, name='winter_0'),
	# url(r'^winter_1/$', views.winter_1, name='winter_1'),
	# url(r'^winter_2/$', views.winter_2, name='winter_2'),
	# url(r'^winter_3/$', views.winter_3, name='winter_3'),
	# url(r'^saleoffuel/$', views.saleoffuel, name='saleoffuel'),
	# url(r'^transportationoffuel/$', views.transportationoffuel, name='transportationoffuel'),
	# url(r'^fuelpumping/$', views.fuelpumping, name='fuelpumping'),
	# url(r'^fuelutilization/$', views.fuelutilization, name='fuelutilization'),
	# url(r'^rentofcontainers/$', views.rentofcontainers, name='rentofcontainers'),
	# url(r'^gasolinetankerrental/$', views.gasolinetankerrental, name='gasolinetankerrental'),
	# url(r'^miniazs/$', views.miniazs, name='miniazs'),
	# url(r'^oilstoragedepot/$', views.oilstoragedepot, name='oilstoragedepot'),
	# url(r'^cooperation/$', views.cooperation, name='cooperation'),
	# url(r'^queandanswers/$', views.queandanswers, name='queandanswers'),
	# url(r'^qualitypassportdt/$', views.qualitypassportdt, name='qualitypassportdt'),
	# url(r'^qualitypassportai/$', views.qualitypassportai, name='qualitypassportai'),
    url(r'^$', views.indexoil, name='indexoil'),
	url(r'^contacts/$', views.contacts, name='contacts'),
	url(r'^certificates/$', views.certificates, name='certificates'),
	url(r'^contactView/$', views.contactView, name='contactView'),
	url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^dieselfuel/$', views.dieselfuel, name='dieselfuel'),
    url(r'^rent/$', views.rent, name='rent'),
    url(r'^gasfilling/$', views.gasfilling, name='gasfilling'),
    url(r'^realization/$', views.realization, name='realization'),
    url(r'^techwork/$', views.techwork, name='techwork'),
        	
	
]