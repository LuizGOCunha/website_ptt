from django.core.exceptions import ValidationError

from validate_docbr import PIS


def pis_validator(client_pis):
    pis = PIS()
    valid = pis.validate(client_pis)
    if not valid:
        raise ValidationError("PIS not valid")
