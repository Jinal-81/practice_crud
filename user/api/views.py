from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from rest_framework import generics
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer, MyTokenObtainPairSerializer, UserSerializer
from ..custom_mixin import CustomPermissionMixin
from ..permissions import IsOwnerOrReadOnly

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.none()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserListView(ListAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer