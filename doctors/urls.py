from django.urls import path

from doctors.views import create, create_appointment
from healing import settings
from django.conf.urls.static import static

app_name = "doctors"

urlpatterns = [
    path("create/", create, name="create"),
    path("appointments/", create_appointment, name="appointments"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

