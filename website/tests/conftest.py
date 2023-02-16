import pytest

from website.models import Address


@pytest.fixture()
def address_object():
    street = "Rua Exemplo Teste"
    number = 228
    city = "Fortaleza"
    state = "Ceará"
    country = "Brazil"
    complement = "Casa 8"
    zipcode = "59147-230"
    address = Address.objects.create(
        street=street,
        number=number,
        city=city,
        state=state,
        country=country,
        complement=complement,
        zipcode=zipcode,
    )
    return address
