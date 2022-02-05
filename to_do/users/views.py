from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer] # this only JSON for frontend
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
