from django.urls import path

from .controllers import GetAllUsers, CreateUser, DeleteUser

urlpatterns = [
    path("", GetAllUsers.as_view(), name="get-all-users"),
    path("create-user", CreateUser.as_view(), name="create-user"),
    path("delete/<int:user_id>", DeleteUser.as_view(), name="delete-user"),
]