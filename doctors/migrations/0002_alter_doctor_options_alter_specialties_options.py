# Generated by Django 5.0.4 on 2024-04-16 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("doctors", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="doctor",
            options={"verbose_name": "Médico", "verbose_name_plural": "Médicos"},
        ),
        migrations.AlterModelOptions(
            name="specialties",
            options={
                "verbose_name": "Especialidade",
                "verbose_name_plural": "Especialidades",
            },
        ),
    ]
