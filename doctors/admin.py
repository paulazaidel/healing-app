from django.contrib import admin

from doctors.models import Doctor, Specialties

admin.site.register(Specialties)
admin.site.register(Doctor)
