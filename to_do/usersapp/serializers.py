from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import User


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        # fields = '__all__'

        # def create(self, validated_data):
        #     return User(**validated_data)


class UserBasedModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')








