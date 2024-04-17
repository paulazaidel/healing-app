from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.messages import add_message, constants

from doctors.models import Doctor, Specialties

def _is_medico(user):
    return Doctor.objects.filter(user=user).exists()

@login_required
def create(request):
    if _is_medico(request.user):
            add_message(request, constants.ERROR, 'Você já é um médico.')
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

        add_message(request, constants.SUCCESS, 'Cadastro médico realizado com sucesso.')
        return redirect("doctors:appointments")
