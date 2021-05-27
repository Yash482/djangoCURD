from rest_framework.response import Response
from app.models import Item
from app.BO.productBO import ItemBO
from app.serializers import ItemSerializer
import json


def addProduct(itemData):
    serializer = ItemSerializer(data = itemData)
    if serializer.is_valid():  
        serializer.save()
        return serializer.data
    return serializer.errors

def updateProduct(itemData):
    serializer = ItemSerializer(Item, data = itemData)
    if(serializer.is_valid()):
        serializer.save()
        return serializer.data
    return serializer.errors

def makeInactive(id):  
    Item.objects.filter(id=id).update(active = True)
    return
