import pytest

from website.models import Address, UserPTT


@pytest.fixture()
def address_object(db):
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

@pytest.fixture()
def user_object(db, address_object):
    name = "Nome Teste"
    email = "Test@nome.com"
    cpf = "59780510117"
    pis = "55030633580"
    password = "123456"
    user = UserPTT.objects.create(
        name=name,
        email=email,
        cpf=cpf,
        pis=pis,
        password=password,
        address=address_object,
    )
    return user
