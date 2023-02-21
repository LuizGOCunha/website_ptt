from rest_framework.viewsets import ModelViewSet

from website.models import UserPTT, Address
from .serializer import UserPTTSerializer, AddressSerializer


class UserPTTViewset(ModelViewSet):
    queryset = UserPTT.objects.all()
    serializer_class = UserPTTSerializer


class AddressViewset(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
