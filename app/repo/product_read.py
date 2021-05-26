from app.models import Item
from app.BO.productBO import ItemBO

def allProducts():
    items = Item.objects.filter(active = False).values
    itemsList = [copyProduct(obj) for obj in items]  
    return itemsList

def oneProduct(id):
    item = Item.objects.get(id=id)
    itemList = [copyProduct(obj) for obj in item]
    return itemList[0]

def copyProduct(data):
    #print(data)
    newItem = ItemBO()
    newItem.id = data['id']
    newItem.product_name  = data['product_name']
    newItem.extra_name = str(data['extra_name'])
    newItem.weight_info = data['weight_info']
    newItem.packaging_info = data['packaging_info']
    newItem.packaging_type = data['packaging_type']
    newItem.expired_on = str(data['expired_on'])
    newItem.is_frozen = data['is_frozen']
    newItem.active  = data['active']
    newItem.created_on = str(data['created_on'])
    newItem.updated_on = str(data['updated_on'])
    return newItem