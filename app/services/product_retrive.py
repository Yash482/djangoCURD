from app.repo.product_read import allProducts, oneProduct
from app.BO.productBO import ItemBO

def getAllProducts():
    return allProducts()

def getProductById(id):
    return oneProduct(id)
