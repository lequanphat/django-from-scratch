from django.urls import path

from .controllers import GetAllCategory,CreateCategory,DeleteCategory

urlpatterns = [
    path("", GetAllCategory.as_view(), name="get-all-categories"),
    path("create-category", CreateCategory.as_view(), name="create-category"),
    path("delete/<int:catefory_id>", DeleteCategory.as_view(), name="delete-category"),
]