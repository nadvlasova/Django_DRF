from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from project.models import Project, TODO
# from usersapp import serializers


class ProjectModelSerializer(ModelSerializer):
    # users_list = serializers.UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('name', 'link_to_repo', 'user_list')


class TODOModelSerializer(ModelSerializer):
    date_create = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    date_update = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    # creator = serializers.UserModelSerializer(creator='username')


    class Meta:
        model = TODO
        fields = '__all__'
        # fields = ('name_project', 'creator',)
        project_name = ProjectModelSerializer('name')


