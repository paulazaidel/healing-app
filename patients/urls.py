from django.urls import path

from patients.views import home, schedule_appointment


app_name = "patients"

urlpatterns = [
    path("home/", home, name="home"),
    path("schedule_appointment/<int:doctor_id>/", schedule_appointment, name="schedule_appointment"),
]