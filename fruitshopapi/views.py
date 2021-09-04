from .models import Fruitmodel,usermodel,cartmodel,favmodel
from .serializers import FruitSerializer,UserSerializer,cartSerializer,favSerializer
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
        fruits=serializer.data
        
        for x in fruits:
         print(x)
         if x == 'banana':
           continue
         print(x)
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
        queryset=cartmodel.objects.filter(userid=data['productid'])
        if len(queryset)==0:
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
            queryset=cartmodel.objects.all()
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
        queryset=usermodel.objects.filter(username=data['username'])
        checkserializer=UserSerializer(queryset,many=True)
        if len(checkserializer.data)==0:
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"response": {"data": "success","error":"null"}}, status=200)
            return JsonResponse({"response": {"data": "null","error":serializer.errors}}, status=400)
        return JsonResponse({"response": {"data": "null","error":"email_already_exists"}}, status=400)



@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            queryset=usermodel.objects.filter(username=data['username'])
            serializer=UserSerializer(queryset,many=True)
            if len(serializer.data)==0:
                return JsonResponse({"response": {"data": 'null',"error":'user_not_found'}}, status=400)
            if serializer.data[0]['password']==data['password']:
                return JsonResponse({"response": {"data": serializer.data,"error":'null'}}, safe=False)
            return JsonResponse({"response": {"data": 'null',"error":'Wrong_password'}}, status=400)
        except:
            return JsonResponse(serializer.errors, status=400)




@csrf_exempt
def addfav(request):
    if request.method == 'GET':
        queryset=favmodel.objects.all()
        serializer=favSerializer(queryset,many=True)
        return JsonResponse({"response": {"data": serializer.data,"error":'null'}}, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        queryset=usermodel.objects.filter(userid=data['userid'])
        serializer1=UserSerializer(queryset,many=True)
        if len(serializer1.data)==0:
            return JsonResponse({"response": {"data": 'null',"error":'user_not_found'}}, status=400)

        queryset1=favmodel.objects.filter(productid=data['productid'])
        serializer2=favSerializer(queryset1,many=True)
        if data['isfav']=='false':
            if len(serializer2.data)==0:
                return JsonResponse({"response": {"data": 'null',"error":'product_not_found_on_your_fav'}}, status=400)
            queryset1.delete()
        elif data['isfav']=='true':
            serializer = favSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"response": {"data": "success"}}, status=200)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"response": {"data": 'null',"error":'something_went_wrong'}}, status=400)

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