import datetime

from django.contrib.auth.models import User
from django.db import models


class Appointments(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    has_patient = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"


class Specialties(models.Model):
    specialty = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="icons", null=True, blank=True)

    def __str__(self):
        return self.specialty

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"


class Doctor(models.Model):
    crm = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    street = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street_number = models.IntegerField()
    rg = models.ImageField(upload_to="rgs")
    medical_identity = models.ImageField(upload_to="cim")
    photo = models.ImageField(upload_to="fotos_perfil")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    specialty = models.ForeignKey(
        Specialties, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    appointment_price = models.FloatField(default=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

    @property
    def next_open_date(self):
        appointment = (
            Appointments.objects.filter(user=self.user)
            .filter(date__gt=datetime.datetime.now())
            .filter(has_patient=False)
            .order_by("date")
            .first()
        )
        return appointment.date if appointment else None
