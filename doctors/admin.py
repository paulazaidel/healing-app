from django.contrib import admin

from doctors.models import Appointments, Doctor, Specialties

admin.site.register(Specialties)
admin.site.register(Doctor)
admin.site.register(Appointments)
