from app.repo.product_write import makeInactive, updateProduct
from app.BO.productBO import ItemBO

def callUpdateProduct(data):
    updatedItem = updateProduct( data)
    return updatedItem

def removeProduct(id):
    makeInactive(id)
    return


