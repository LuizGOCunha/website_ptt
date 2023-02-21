import pytest

from django.test import Client, RequestFactory
from django.urls import reverse

@pytest.mark.django_db
class TestIndexView:
    client = Client()
    factory = RequestFactory()

    def test_if_api_root_is_accessible(self, user_object, address_object):
        response = self.client.get(reverse("api-root"))
        assert response.status_code == 200

    def test_if_users_endpoint_is_accessible(self, user_object):
        response = self.client.get(reverse("users-list"))
        assert response.status_code == 200
        response = self.client.get(reverse("users-detail", args=["1"]))
        assert response.status_code == 200

    def test_if_addresses_endpoint_is_accessible(self, address_object):
        response = self.client.get(reverse("addresses-list"))
        assert response.status_code == 200
        response = self.client.get(reverse("addresses-detail", args=["1"]))
        assert response.status_code == 200

    def test_if_users_endpoint_presents_right_data(self, user_object, signup_data):
        response = self.client.get(reverse("users-detail", args=["1"]))
        response_data = response.json()
        assert response_data["name"] == signup_data["name"]
        assert response_data["pis"] == signup_data["pis"]
        assert response_data["cpf"] == signup_data["cpf"]
        assert response_data["email"] == signup_data["email"]

    def test_if_addresses_endpoint_presents_right_data(self, address_object, signup_data):
        response = self.client.get(reverse("addresses-detail", args=["1"]))
        response_data = response.json()
        assert response_data["street"] == signup_data["street"]
        assert response_data["number"] == signup_data["number"]
        assert response_data["complement"] == signup_data["complement"]
        assert response_data["city"] == signup_data["city"]
        assert response_data["state"] == signup_data["state"]
        assert response_data["country"] == signup_data["country"]

    def test_if_we_can_retrieve_our_jwt_token(self, user_object, signup_data):
        response = self.client.post(reverse("token_obtain_pair"), data={
            "email": signup_data["email"],
            "password": signup_data["password"]
        })
        assert response.status_code == 200
        assert response.json()["access"]
        assert response.json()["refresh"]