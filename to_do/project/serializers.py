from rest_framework.serializers import HyperlinkedModelSerializer

from project.models import Project, TODO


class ProjectModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        # fields = '__all__'
        fields = 'first_name'


class TODOModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = TODO
        # fields = '__all__'
        fields = 'last_name'