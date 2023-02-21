from rest_framework import serializers

from website.models import UserPTT, Address

class UserPTTSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPTT
        fields = ['name', 'email', 'cpf', 'pis', 'address']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"