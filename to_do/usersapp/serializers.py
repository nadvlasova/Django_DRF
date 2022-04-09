from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import User


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        # fields = '__all__'
        # exclude = ('email')


class UserBasedModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


# class UsersListSerializer(UserModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username')





