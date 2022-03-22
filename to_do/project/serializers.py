from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from project.models import Project, TODO


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('name', 'link_to_repo', 'user_list')


class TODOModelSerializer(ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
        # fields = ('name_project', 'creator',)
