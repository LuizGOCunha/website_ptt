from django.core.exceptions import ValidationError

from website.models import Address, UserPTT

import pytest


@pytest.mark.django_db
class TestAddressModel:
    def test_if_we_can_create_a_proper_address_object(self):
        street = "Rua Exemplo Teste"
        number = 228
        city = "Fortaleza"
        state = "Ceará"
        country = "Brazil"
        complement = "Casa 8"
        zipcode = "59147-230"
        Address.objects.create(
            street=street,
            number=number,
            city=city,
            state=state,
            country=country,
            complement=complement,
            zipcode=zipcode,
        )
        assert Address.objects.count() == 1
        address_db = Address.objects.first()
        assert address_db.street == street
        assert address_db.number == number
        assert address_db.city == city
        assert address_db.state == state
        assert address_db.country == country
        assert address_db.complement == complement
        assert address_db.zipcode == zipcode


@pytest.mark.django_db
class TestUserModel:
    def test_if_we_can_create_a_proper_user(self, address_object):
        name = "Nome Teste"
        email = "Test@nome.com"
        cpf = "59780510117"
        pis = "55030633580"
        password = "123456"
        user = UserPTT(
            name=name,
            email=email,
            cpf=cpf,
            pis=pis,
            password=password,
            address=address_object,
        )
        user.full_clean()
        user.save()
        assert UserPTT.objects.count() == 1
        user = UserPTT.objects.first()
        assert user.name == name
        assert user.email == email
        assert user.cpf == cpf
        assert user.pis == pis
        # password encrypted
        assert user.check_password(password)

    def test_if_we_can_create_improper_user(self, address_object):
        with pytest.raises(ValidationError):
            name = "Nome Teste"
            email = "Test@nome.com"
            cpf = "59780510117"
            pis = "sad"
            password = "123456"
            user = UserPTT(
                name=name,
                email=email,
                cpf=cpf,
                pis=pis,
                password=password,
                address=address_object,
            )
            user.full_clean()
        with pytest.raises(ValidationError):
            name = "Nome Teste"
            email = "Test@nome.com"
            cpf = "123"
            pis = "55030633580"
            password = "123456"
            user = UserPTT(
                name=name,
                email=email,
                cpf=cpf,
                pis=pis,
                password=password,
                address=address_object,
            )
            user.full_clean()
