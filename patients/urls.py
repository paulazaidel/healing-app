from django.urls import path

from patients.views import (
    appointments,
    consulta,
    home,
    new_schedule_appointment,
    schedule_appointment,
)

app_name = "patients"

urlpatterns = [
    path("home/", home, name="home"),
    path(
        "schedule_appointment/<int:doctor_id>/",
        schedule_appointment,
        name="schedule_appointment",
    ),
    path(
        "schedule_appointment/new/<int:appointment_id>/",
        new_schedule_appointment,
        name="new_schedule_appointment",
    ),
    path(
        "schedule_appointment/",
        appointments,
        name="appointments",
    ),
    path(
        "consulta/<int:appointment_id>/",
        consulta,
        name="consulta",
    ),
]
