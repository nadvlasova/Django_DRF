from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from project.models import Project, TODO
from usersapp import serializers


class ProjectModelSerializer(ModelSerializer):
    users_list = serializers.UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('name', 'link_to_repo', 'user_list')


class TODOModelSerializer(ModelSerializer):
    # creator = serializers.UserModelSerializer()
    # project_name = ProjectModelSerializer()

    class Meta:
        model = TODO
        fields = '__all__'
        # fields = ('name_project', 'creator',)


