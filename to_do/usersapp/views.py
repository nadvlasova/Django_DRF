from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserModelSerializer, UserBasedModelSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserBasedModelSerializer  # fields = ('first_name', 'last_name')
        return UserModelSerializer  # (fields = ('username', 'first_name', 'last_name', 'email')







# class UserModelViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer] # this only JSON for frontend
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
#
# class UserCreateAPIView(CreateAPIView):
#     renderer_classes = [JSONRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
#
# class UserListAPIView(ListAPIView):
#     renderer_classes = [JSONRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
#
# class UserRetrieveAPIView(RetrieveAPIView):
#     renderer_classes = [JSONRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
