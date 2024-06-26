from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("doctors/", include("doctors.urls")),
    path("patients/", include("patients.urls")),
]
