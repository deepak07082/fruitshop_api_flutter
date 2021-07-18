from django.contrib import admin
from django.urls import path
# from rest_framework import views
from fruitshopapi import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('fruits/',views.fruitview,name='fruitview' ),
    path('fruitslist/',views.fruitslistview,name='fruitslistview' ),
    path('img/',views.imgsnd,name='imgsnd' ),
    path('fruits/<int:id>/', views.fetchfruit ,name='spcificfruits'),
    path('users/',views.adduser,name='usercrud' ),
    path('cart/',views.addcart,name='addcart' ),
    path('fetchcart/',views.fetchcart,name='getcart' ),
    path('deletecart/',views.deletecart,name='deletecart' ),
]


urlpatterns+=staticfiles_urlpatterns()