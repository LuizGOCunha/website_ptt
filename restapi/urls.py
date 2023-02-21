from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .viewset import UserPTTViewset, AddressViewset


router = routers.DefaultRouter()
router.register(r"users", UserPTTViewset, basename="users")
router.register(r"addresses", AddressViewset, basename="addresses")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
