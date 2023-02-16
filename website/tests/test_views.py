import pytest

from django.test import Client, RequestFactory
from django.urls import reverse
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from website.views import signup
from website.models import UserPTT, Address


@pytest.mark.django_db
class TestIndexView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("index"))
        assert response.status_code == 200


@pytest.mark.django_db
class TestSignupView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("signup"))
        assert response.status_code == 200

    def test_if_we_can_create_user_and_address_through_view(self, signup_data):
        self.client.post(path=reverse("signup"), data=signup_data)
        assert UserPTT.objects.count() == 1
        user = UserPTT.objects.first()
        assert user.name == signup_data["name"]
        assert user.email == signup_data["email"]
        assert user.cpf == signup_data["cpf"]
        assert user.pis == signup_data["pis"]
        assert user.check_password(signup_data["password"])

        assert Address.objects.count() == 1
        address = Address.objects.first()
        assert user.address == address
        assert address.country == signup_data["country"]
        assert address.city == signup_data["city"]
        assert address.street == signup_data["street"]
        assert address.number == signup_data["number"]
        assert address.complement == signup_data["complement"]
        assert address.zipcode == signup_data["zipcode"]

    def test_to_see_if_we_can_handle_existing_user_error(self, signup_data):
        request = self.factory.post(path=reverse("signup"), data=signup_data)
        response = signup(request)
        # If registrations successful, the view will redirect to signin page, returning 302
        assert response.status_code == 302

        with pytest.raises(ValidationError):
            response2 = signup(request)
            # If encountering an error, page will reload, returning 200
            assert response2.status_code == 200


@pytest.mark.django_db
class TestSigninView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("signin"))
        assert response.status_code == 200

    def test_if_we_can_login_through_view(self, user_object, signup_data):
        response = self.client.post(
            path=reverse("signin"),
            data={"email": signup_data["email"], "password": signup_data["password"]},
        )
        # When signin is successful, redirects to homepage, returning 302
        assert response.status_code == 302
        assert self.client.session.session_key, "Failed to create session"


@pytest.mark.django_db
class TestSignoutView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("signout"))
        # signout is a redirect, normally it returns a 302
        assert response.status_code == 302
