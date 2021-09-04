from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Fruitmodel,usermodel,cartmodel,favmodel


@admin.register(Fruitmodel)
class FruitAdmin(admin.ModelAdmin):
    list_display=['fruitname','price','desc','favourite','imgpath','rating','color']

@admin.register(usermodel)
class userAdmin(admin.ModelAdmin):
    list_display=['username','password','userid']

@admin.register(cartmodel)
class cartAdmin(admin.ModelAdmin):
    list_display=['productid','userid']


@admin.register(favmodel)
class favourites(admin.ModelAdmin):
    list_display=['productid','userid','isfav']
