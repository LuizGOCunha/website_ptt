from django.urls import path, include

from rest_framework import routers
from .viewset import UserPTTViewset, AddressViewset

router = routers.DefaultRouter()
router.register(r"users", UserPTTViewset, basename="users")
router.register(r"addresses", AddressViewset, basename="addresses")

urlpatterns = [
    path("", include(router.urls))
]