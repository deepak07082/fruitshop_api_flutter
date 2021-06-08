from .models import Fruitmodel
from .serializers import FruitSerializer
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
import base64

@csrf_exempt
def fruitview(request):
    if request.method == 'GET':
        queryset=Fruitmodel.objects.all()
        serializer=FruitSerializer(queryset,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FruitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"response": {"data": "success"}}, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def fetchfruit(request,id):
    
    try:
        snippet = Fruitmodel.objects.get(id=id)

    except: 
        return HttpResponse(status=400)   
    if request.method == 'GET':
        serializer = FruitSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
        

@csrf_exempt
def imgsnd(request):
    return 'assets/pic_pineapple.png'