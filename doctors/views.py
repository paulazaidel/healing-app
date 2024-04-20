import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.messages import add_message, constants
from django.shortcuts import redirect, render

from doctors.models import Appointments, Doctor, Specialties
from patients.models import PatientAppointment


def _is_medico(user):
    return Doctor.objects.filter(user=user).exists()


@login_required
def create(request):
    if _is_medico(request.user):
        add_message(request, constants.ERROR, "Você já é um médico.")
        return redirect("doctors:appointments")
    elif request.method == "GET":
        specialties = Specialties.objects.all()
        return render(request, "create_doctor.html", {"specialties": specialties})
    elif request.method == "POST":
        crm = request.POST.get("crm")
        cim = request.FILES.get("cim")
        name = request.POST.get("name")
        cep = request.POST.get("cep")
        street = request.POST.get("street")
        neighborhood = request.POST.get("neighborhood")
        street_number = request.POST.get("street_number")
        rg = request.FILES.get("rg")
        photo = request.FILES.get("photo")
        specialty_id = request.POST.get("specialty")
        description = request.POST.get("description")
        appointment_price = request.POST.get("appointment_price")

        doctor = Doctor(
            user=request.user,
            crm=crm,
            medical_identity=cim,
            name=name,
            cep=cep,
            street=street,
            neighborhood=neighborhood,
            street_number=street_number,
            rg=rg,
            photo=photo,
            specialty_id=specialty_id,
            description=description,
            appointment_price=appointment_price,
        )
        doctor.save()

        add_message(
            request, constants.SUCCESS, "Cadastro médico realizado com sucesso."
        )
        return redirect("doctors:appointments")


@login_required
def create_appointment(request):
    if not _is_medico(request.user):
        add_message(
            request, constants.WARNING, "Somente médicos podem acessar essa página."
        )
        return redirect("users:logout")
    elif request.method == "GET":
        doctor = Doctor.objects.get(user=request.user)
        appointments = Appointments.objects.filter(user=request.user)

        return render(
            request,
            "create_appointment.html",
            {"doctor": doctor, "appointments": appointments},
        )
    elif request.method == "POST":
        date = request.POST.get("date")
        date_formatted = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M")

        if date_formatted < datetime.datetime.now():
            add_message(
                request, constants.ERROR, "A data deve ser maior ou igual a data atual."
            )
            return redirect("doctors:appointments")

        appointment = Appointments(date=date, user=request.user)
        appointment.save()

        add_message(request, constants.SUCCESS, "Horário cadastrado com sucesso.")
        return redirect("doctors:appointments")


def doctor_appointments(request):
    if not _is_medico(request.user):
        add_message(
            request, constants.WARNING, "Somente médicos podem acessar essa página."
        )
        return redirect("users:logout")

    today = datetime.datetime.now()

    appointments_today = PatientAppointment.objects.filter(
        date__user=request.user,
        date__date__gte=datetime.datetime.now(),
        date__date__lt=today + datetime.timedelta(days=1),
    )
    appointments = PatientAppointment.objects.exclude(
        id__in=appointments_today.values("id")
    )

    return render(
        request,
        "appointments_doctor.html",
        {"appointments": appointments, "appointments_today": appointments_today},
    )
