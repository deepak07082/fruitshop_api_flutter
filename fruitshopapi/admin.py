from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Fruitmodel
# Register your models here.
@admin.register(Fruitmodel)
class FruitAdmin(admin.ModelAdmin):

# # ModelAdmin.site.register(Fruits)

    list_display=['fruitname','price','desc','favourite','imgpath','rating','color']
