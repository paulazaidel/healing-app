from django.db import models
from django.contrib.auth.models import User

from doctors.models import Appointments

class PatientAppointment(models.Model):
    status_choices = (
        ('A', 'Agendada'),
        ('F', 'Finalizada'),
        ('C', 'Cancelada'),
        ('I', 'Iniciada')
    )

    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.ForeignKey(Appointments, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=status_choices, default='A')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name = "Paciente - Consulta"
        verbose_name_plural = "Paciente - Consultas"
