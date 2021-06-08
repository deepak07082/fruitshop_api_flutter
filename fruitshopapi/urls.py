from django.contrib import admin
from django.urls import path
# from rest_framework import views
from fruitshopapi import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('fruits/',views.fruitview,name='fruitview' ),
    path('img/',views.imgsnd,name='imgsnd' ),
    path('fruits/<int:id>/', views.fetchfruit ,name='spcificfruits'),
]


urlpatterns+=staticfiles_urlpatterns()