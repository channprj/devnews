# django
from django.contrib.auth import get_user_model
from django.shortcuts import render

# third-party
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response


# serializers
from .serializers import UserSerializer
from .serializers import ProfileSerializer

# models
from .models import Profile


UserModel = get_user_model()


@api_view(['get'])
@permission_classes((permissions.AllowAny,))
def health_check(request):
    return Response({'status': 'ok'})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserModel.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
