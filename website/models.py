from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password

from .validators import pis_validator

from cpf_field.models import CPFField


class UserPTTManager(models.Manager):
    def get_by_natural_key(self, email):
        return self.get(email=email)


class Address(models.Model):
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zipcode = models.CharField("Zip-code", max_length=50)
    street = models.CharField(max_length=150)
    number = models.IntegerField()
    complement = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        if self.complement:
            full_address = (
                f"{self.street} {self.number}, {self.complement}; {self.city}, {self.state}, {self.country}"
            )
        else:
            full_address = (
                f"{self.street} {self.number}; {self.city}, {self.state}, {self.country}"
            )
        return full_address


class UserPTT(AbstractBaseUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name="user"
    )
    last_login = models.DateTimeField(auto_now_add=True)
    # Validation required!
    cpf = CPFField("CPF")
    # Validation required!
    pis = models.CharField(
        "PIS",
        max_length=11,
        validators=[
            pis_validator,
        ],
    )
    objects = UserPTTManager()

    USERNAME_FIELD = "email"

    # By partially overriding this method, we can encrypt our password.
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserPTT, self).save(*args, **kwargs)
