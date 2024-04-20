from django.conf.urls.static import static
from django.urls import path

from doctors.views import create, create_appointment, doctor_appointments
from healing import settings

app_name = "doctors"

urlpatterns = [
    path("create/", create, name="create"),
    path("appointments/", create_appointment, name="appointments"),
    path(
        "appointments/all",
        doctor_appointments,
        name="appointments_all",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
