from django.db import models

class Fruitmodel(models.Model):
    fruitname=models.CharField(max_length=40)
    price=models.IntegerField()
    desc=models.CharField(max_length=300)
    favourite=models.BooleanField()
    imgpath=models.CharField(max_length=40)
    rating=models.IntegerField()
    color=models.CharField(max_length=20)