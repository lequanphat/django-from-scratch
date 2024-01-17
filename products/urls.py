from django.urls import path

from .views import GetAllProduct, CreateProduct, DeleteProduct

urlpatterns = [
    path("", GetAllProduct.as_view(), name="get-all-product"),
    path("create-product", CreateProduct.as_view(), name="create-product"),
    path("delete/<int:product_id>", DeleteProduct.as_view(), name="delete-product"),
]