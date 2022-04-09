from django.db.models import ForeignKey
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from project.models import Project, TODO
from usersapp.models import User


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('name', 'link_to_repo', 'user_list')


# class UserListSerializer(UserModelSerializer):
#     class Meta:
#         model = User
#         fields = 'username'


class TODOModelSerializer(ModelSerializer):
    date_create = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", default=True)
    date_update = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", default=True)
    creator = serializers.CharField(max_length=64)
    # name_project = ProjectModelSerializer(instance='name', data={'name'}, partial=True)
    # name_project = ProjectModelSerializer(data={'name'}, partial=True)

    # name_project = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.filter(name=True))
    name_project = ProjectModelSerializer(Project.objects.name)

    class Meta:
        model = TODO
        fields = '__all__'
        # fields = ('name_project', 'creator',)

    # def create(self, validated_data):
    #     name_project = Project.objects.name
    #     return name_project
