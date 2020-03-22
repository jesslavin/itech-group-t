from django.conf.urls import url
from django.urls import path
from django.urls import include
from vinyldestination import views

app_name = 'vinyldestination'
urlpatterns = [
    path('', views.index, name='index'),
    path('artists/', views.artists, name='artists'),
    path('records/', views.records, name='records'),
    path('artists/<slug:artist_name_slug>/', views.show_artist,
        name='show_artist'),

    path('register/', views.register, name='register'), 
    path('restricted/', views.restricted, name='restricted'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

# path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('category/<slug:category_name_slug>/add_page/', views.add_page,
#         name='add_page'),
#     path('category/<slug:category_name_slug>/', views.show_category,
#         name='show_category'),

