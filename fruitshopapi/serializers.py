from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Fruitmodel,usermodel,cartmodel,favmodel


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fruitmodel
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=usermodel
        fields='__all__'

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model=cartmodel
        fields='__all__'


class favSerializer(serializers.ModelSerializer):
    class Meta:
        model=favmodel
        fields='__all__'
       