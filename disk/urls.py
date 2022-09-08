from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('threeCar', views.threeCar, name='threeCar'),
    path('love', views.love, name='love'),
    path('drink', views.drink, name='drink'),
    path('moon', views.moon, name='moon'),
    path('audio', views.audio, name='audio'),
    path('video', views.video, name='video'),
    path('eye', views.eye, name='eye'),
    path('Dback', views.Dback, name='Dback'),
    path('Click', views.Click, name='Click'),
    path('Road', views.Road, name='Road'),
    path('Social', views.Social, name='Social'),
    path('Color', views.Color, name='Color'),
    path('pixsar', views.pixsar, name='pixsar'),
    path('Dark', views.Dark, name='Dark'),

]