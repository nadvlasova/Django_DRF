from django_filters import rest_framework as filters, IsoDateTimeFilter
from .models import Project, TODO


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TODOFilter(filters.FilterSet):
    # name_project = filters.CharFilter(lookup_expr='contains')
    # date_create = IsoDateTimeFilter()
    # date_update = IsoDateTimeFilter()
    date_create = filters.DateFromToRangeFilter()

    class Meta:
        model = TODO
        fields = ['name_project', 'date_create']

