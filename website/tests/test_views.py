import pytest

from django.test import Client, RequestFactory
from django.urls import reverse

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


@pytest.mark.django_db
class TestSigninView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("signin"))
        assert response.status_code == 200