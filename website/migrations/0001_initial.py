# Generated by Django 4.1.7 on 2023-02-16 13:25

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion
import website.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", models.CharField(max_length=150)),
                ("state", models.CharField(max_length=150)),
                ("city", models.CharField(max_length=150)),
                ("zipcode", models.CharField(max_length=50, verbose_name="Zip-code")),
                ("street", models.CharField(max_length=150)),
                ("number", models.IntegerField()),
                ("complement", models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserPTT",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("cpf", cpf_field.models.CPFField(max_length=14, verbose_name="CPF")),
                (
                    "pis",
                    models.CharField(
                        max_length=11,
                        validators=[website.validators.pis_validator],
                        verbose_name="PIS",
                    ),
                ),
                (
                    "address",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to="website.address",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]