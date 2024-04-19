import datetime

from django.contrib.messages import add_message, constants
from django.shortcuts import redirect, render

from doctors.models import Appointments, Doctor, Specialties
from patients.models import PatientAppointment


def home(request):
    if request.method == "GET":
        doctor_filter = request.GET.get("doctor_filter")
        specialties_filter = request.GET.getlist("specialties_filter")

        doctors = Doctor.objects.all()

        if doctor_filter:
            doctors = doctors.filter(name__icontains=doctor_filter)

        if specialties_filter:
            doctors = doctors.filter(specialty_id__in=specialties_filter)

        specialties = Specialties.objects.all()
        return render(
            request, "home.html", {"doctors": doctors, "specialties": specialties}
        )


def schedule_appointment(request, doctor_id):
    if request.method == "GET":
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointments.objects.filter(
            user=doctor.user, date__gte=datetime.datetime.now(), has_patient=False
        )
        return render(
            request,
            "schedule_appointment.html",
            {"doctor": doctor, "appointments": appointments},
        )


def new_schedule_appointment(request, appointment_id):
    if request.method == "GET":
        appointment = Appointments.objects.get(id=appointment_id)

        patient_appointment = PatientAppointment(
            patient=request.user, date=appointment, status="A"
        )

        patient_appointment.save()
        appointment.has_patient = True
        appointment.save()

        add_message(request, constants.SUCCESS, "Horário agendado com sucesso.")
        return redirect("patients:home")
