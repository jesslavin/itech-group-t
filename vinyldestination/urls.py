from django.conf.urls import url
from django.urls import path
from django.urls import include
from vinyldestination import views

app_name = 'vinyldestination'
urlpatterns = [
    path('', views.index, name='index'),
    path('artists/', views.artsits, name='artists'),
    path('register/', views.register, name='register'), 
    path('restricted/', views.restricted, name='restricted'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

