from app.models import Item
from app.BO.productBO import ItemBO
from app.serializers import ItemSerializer

def allProducts():
    items = Item.objects.all()
    serialised = ItemSerializer(items, many = True)
    return serialised.data

def oneProduct(id):
    item = Item.objects.get(id= id)
    serialised = ItemSerializer(item, many = False)
    return serialised.data

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