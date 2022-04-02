from rest_framework.serializers import ModelSerializer

from usersapp.models import User


class UserApiSerializer(ModelSerializer):
    class Meta:
        model = User  # это мой юзер в методичке из коробки django.contrib.auth.models
        fields = ('username', 'email')


class UserApiBaseSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ('username', 'email', 'first_name', 'last_name')
        fields = ('is_superuser', 'is_staff')
