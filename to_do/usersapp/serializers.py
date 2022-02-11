from rest_framework.serializers import  HyperlinkedModelSerializer
from .models import User, Project, TODO


class UserModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        # fields = '__all__'
        # exclude = ('email')


class ProjectModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = TODO
        fields = '__all__'

