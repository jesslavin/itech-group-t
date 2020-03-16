from django.conf.urls import url
from django.urls import path
from rango import views

app_name = 'vinyldestination'

urlpatterns = [
    path('', views.index, name='index'),
    path('artsits/', views.artsits, name='artsits'),
    path('artists/<slug:artist_name_slug>/', views.show_artist,
        name='show_artist'),

    # path('category/<slug:category_name_slug>/', views.show_category,
    #     name='show_category'),
    # path('add_category/', views.add_category, name='add_category'),
    # path('register/', views.register, name='register'), 
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('restricted/', views.restricted, name='restricted'),
]