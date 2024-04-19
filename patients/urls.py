from django.urls import path

from patients.views import home


app_name = "patients"

urlpatterns = [
    path("home/", home, name="home"),
]