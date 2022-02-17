from django_filters import rest_framework as filters, IsoDateTimeFilter
from .models import Project, TODO


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TODODateFilter(filters.FilterSet):
    date_create = IsoDateTimeFilter()
    date_update = IsoDateTimeFilter()

    class Meta:
        model = TODO
        fields = ['date_create', 'date_update']

