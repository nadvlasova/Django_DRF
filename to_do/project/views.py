from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from project.models import Project, TODO
from project.serializers import ProjectModelSerializer, TODOModelSerializer


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TODOModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
