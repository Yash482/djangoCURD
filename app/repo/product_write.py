from app.models import Item
from app.BO.productBO import ItemBO


def addProduct(data):
    data.save() 
    return

def updateProduct(id, data):
    Item.objects.filter(id=id).update(
        product_name = data['product_name'],
        extra_name = data['extra_name'].split(","),
        weight_info = data['weight_info'],
        packaging_info = data['packaging_info'],
        packaging_type = data['packaging_type'],
        expired_on = data['expired_on'],
        is_frozen = data['is_frozen']
    ) 

def makeInactive(id):  
    Item.objects.filter(id=id).update(active = True)
    return
