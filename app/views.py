from django.shortcuts import render, redirect
from rest_framework import serializers
from app.forms import ItemForm 
from app.models import Item
from app.services.product_retrive import getAllProducts, getProductById
from app.services.product_update import removeProduct, callUpdateProduct
from app.services.product_creation import callAddProduct
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer
from django.http import HttpResponse
from rest_framework import status

class itemList(APIView):

    def get(self, request):
        itemsList = getAllProducts()
        return Response(itemsList)

class item(APIView):

    def get(self, request, id):
        item = getProductById(id)
        return Response(item)

class addItem(APIView):

    def post(self, request):
        newItem = callAddProduct(request.data)
        return Response(newItem)

class updateItem(APIView):

    def put(self, request, id):
        newItem = callUpdateProduct(request.data)
        return Response(newItem)

class deleteItem(APIView):

    def delete(self, request, id):
        removeProduct(id)
        return Response(status=status.HTTP_204_NO_CONTENT)



