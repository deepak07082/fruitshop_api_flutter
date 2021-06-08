from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Fruitmodel
class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fruitmodel
        fields='__all__'
       