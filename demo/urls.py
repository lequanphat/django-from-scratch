from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/products/", include("products.urls")),
    path("api/categories/", include("categories.urls")),
    path("api/users/", include("users.urls")),
]