from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("logout/", views.logout, name="logout"),
    path("login/", views.login, name="login"),
    path("create/", views.create, name="create"),
]
