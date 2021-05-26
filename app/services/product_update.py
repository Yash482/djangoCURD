from app.repo.product_write import makeInactive, updateProduct
from app.BO.productBO import ItemBO

def callUpdateProduct(id, data):
    updateProduct(id, data)
    return

def removeProduct(id):
    makeInactive(id)
    return


