from .models import Fruitmodel,usermodel,cartmodel
from .serializers import FruitSerializer,UserSerializer,cartSerializer
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
import base64


@csrf_exempt
def fruitview(request):
    if request.method == 'GET':
        queryset=Fruitmodel.objects.all()[:4]
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
def fruitslistview(request):
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
def addcart(request):
    if request.method == 'GET':
        queryset=cartmodel.objects.all()
        serializer=cartSerializer(queryset,many=True)
        return JsonResponse({"response": {"data": serializer.data,"error":'null'}}, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = cartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"response": {"data": "success"}}, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def fetchcart(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            queryset=cartmodel.objects.filter(userid=data['userid'])
            serializer=cartSerializer(queryset,many=True)
            if len(serializer.data)==0:
                return JsonResponse({"response": {"data": 'null',"error":'no_items_found'}}, status=400)
            return JsonResponse({"response": {"data": serializer.data,"error":'null'}}, safe=False)
        except:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def deletecart(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            queryset=cartmodel.objects.get(id=data['id'])
        except:
            return JsonResponse({"response": {"data": 'null',"error":'item_not_found'}}, status=400)
        if queryset is None:
            return JsonResponse(serializer.errors, status=400)
        queryset.delete()
        return JsonResponse({"response": {"data": 'success',"error":'null'}}, safe=False)
       
       


# this view is used to create and fetch the user data
@csrf_exempt
def adduser(request):
    if request.method == 'GET':
        queryset=usermodel.objects.all()
        serializer=UserSerializer(queryset,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"response": {"data": "success"}}, status=200)
        return JsonResponse(serializer.errors, status=400)



# dummy if you want delete items(fruits) use this one
@csrf_exempt
def fetchfruit(request,id):
    try:
        snippet = Fruitmodel.objects.get(id=id)
    except: 
        return HttpResponse(status=400)   
    if request.method == 'GET':
        serializer = FruitSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FruitSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
        
# image fetch url set
@csrf_exempt
def imgsnd(request):
    return 'assets/pic_pineapple.png'