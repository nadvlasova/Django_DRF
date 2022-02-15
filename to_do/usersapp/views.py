from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]  # this only JSON for frontend
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
