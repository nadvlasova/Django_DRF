from django.db.models import ForeignKey
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from project.models import Project, TODO


class ProjectModelSerializer(ModelSerializer):
    # users_list = serializers.UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('name', 'link_to_repo', 'user_list')


class TODOModelSerializer(ModelSerializer):
    date_create = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    date_update = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    creator = serializers.CharField()
    name_project = serializers.CharField()

    class Meta:
        model = TODO
        fields = '__all__'
        # fields = ('name_project', 'creator',)




