from django.shortcuts import render, redirect
from app.forms import ItemForm 
from app.models import Item
from app.services.product_retrive import getAllProducts, getProductById
from app.services.product_update import removeProduct, callUpdateProduct
from app.services.product_creation import callAddProduct
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer

class itemList(APIView):

    def get(self, request):
        items = Item.objects.all()
        serialised = ItemSerializer(items, many = True)
        return Response(serialised.data)

class item(APIView):

    def get(self, request, id):
        items = Item.objects.get(id= id)
        serialised = ItemSerializer(items, many = False)
        return Response(serialised.data)

class addItem(APIView):

    def post(self, request):
        form = ItemForm(request.POST)  
        if form.is_valid():  
            try:  
                callAddProduct(form) 
                serialised = ItemSerializer(request.POST, many = False)
                return Response(serialised.data)
            except:  
                return Response("error occured")

# def home(request):
#     itemsList = getAllProducts() 
#     return render(request, 'home.html', {'items' : itemsList})

def addProduct(request):  
    if request.method == "POST":  
        form = ItemForm(request.POST)  
        if form.is_valid():  
            try:  
                callAddProduct(form) 
                return redirect('/')  
            except:  
                pass  
    else:  
        form = ItemForm()  
    return render(request,'add-product.html',{'form':form})  

# def getOneProduct(request, id):
#     item = getProductById(id)
#     return render(request, 'showItem.html', {'item' : item})

def deleteProduct(request, id):  
    removeProduct(id)
    return redirect("/")  

def editProduct(request, id):  
    item = getProductById(id)
    return render(request,'edit-product.html',{ 'item': item})  

def updateProduct(request, id):  
    callUpdateProduct(id, request.POST)              
    return redirect("/")  



