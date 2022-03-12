"""to_do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from project.views import ProjectModelViewSet, TODOCustomViewSet
from user_api.views import UserListAPIView
from usersapp.views import UserModelViewSet

# from usersapp.views import UserCustomViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='to_do',
        default_version='v1',
        description='Project',
        contact=openapi.Contact(email='to_do@mail.ru'),
        license=openapi.License(name='GB License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


router = DefaultRouter()

router.register('usersapp', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TODOCustomViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),

    # path('api/<str:version>/user/', UserListAPIView.as_view()),
    # path('api/user/v1', include('user_api.urls', namespace='v1')),
    # path('api/user/v2', include('user_api.urls', namespace='v2')),

    path('swagger/', schema_view.with_ui('swagger')),
    # path('swagger<str:format>', schema_view.without_ui()),

]
