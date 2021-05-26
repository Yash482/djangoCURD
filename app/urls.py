from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.itemList.as_view()),
    path('add-product', views.addItem.as_view()),
    path('product/<int:id>', views.item.as_view()),
    path('edit-product/<int:id>', views.editProduct),
    path('update-product/<int:id>', views.updateProduct),
    path('delete-product/<int:id>', views.deleteProduct),
]