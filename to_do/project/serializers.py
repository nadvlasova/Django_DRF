from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from project.models import Project, TODO


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('name', 'link_to_repo', 'user_list')


class NameProjectSerializer(ProjectModelSerializer):
    class Meta:
        model = Project
        fields = ['name']


class TODOModelSerializer(ModelSerializer):
    date_create = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", default=True)
    date_update = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", default=True)
    creator = serializers.CharField(max_length=64)
    # name_project = serializers.CharField(max_length=64)

    name_project = NameProjectSerializer(instance='name')
    # name_project = ProjectModelSerializer(instance='name', data={'name'}, partial=True)  # work

    # name_project = ProjectModelSerializer(instance='id', data={'name'}, partial=True)
    # name_project = ProjectModelSerializer(data={'name'}, partial=True)  # work
    # name_project = ProjectModelSerializer(Project.objects.name)  # work
    # name_project = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # on api don't work

    class Meta:
        model = TODO
        fields = '__all__'
        # fields = ('name_project', 'creator',)

    # def create(self, validated_data):
    #     name_project = Project.objects.name
    #     return name_project
