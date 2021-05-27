from app.repo.product_write import addProduct
from app.BO.productBO import ItemBO

def callAddProduct(data):
    newItem = addProduct(data)
    return newItem


