from django.urls import path
from target.views import home
from target import views

urlpatterns = [
	path('', home, name='home'),
	path('contact',views.contact, name='contact'),
	path('about',views.about, name='about'),

	]