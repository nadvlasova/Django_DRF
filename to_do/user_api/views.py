from django.shortcuts import render
from rest_framework.generics import ListAPIView

from user_api.serializers import UserApiBaseSerializer, UserApiSerializer
from usersapp.models import User


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return UserApiBaseSerializer
        return UserApiSerializer
