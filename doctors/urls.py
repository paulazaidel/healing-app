from django.urls import path

from doctors.views import create

app_name = "doctors"

urlpatterns = [
    path("create/", create, name="create"),
]
