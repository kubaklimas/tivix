from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.api.serializers import UserSerializer
from rest_framework.filters import OrderingFilter, SearchFilter


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ["last_name","first_name"]
    ordering_fields = ["last_name","first_name"]
    filter_backends = (
        OrderingFilter,
        SearchFilter,
    )