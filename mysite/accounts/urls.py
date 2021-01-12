from django.urls import path
from accounts import views


urlpatterns = [
    
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', views.logout, name='logout')
]
