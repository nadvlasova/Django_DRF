from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, viewsets.GenericViewSet):

    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer









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
