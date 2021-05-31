from rest_framework import serializers
from .models import User
class GetAllUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'sex', 'phone_number', 'date_of_birth', 'school', 'image', 'password')