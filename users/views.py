# django
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.shortcuts import render

# third-party
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

# utils
from utils import custom_permission

# serializers
from . import serializers

# models
from .models import Profile


UserModel = get_user_model()


@api_view(['get'])
@permission_classes((permissions.AllowAny,))
def health_check(request):
    headers = {'X-HEALTH-CHECK': 'true'}
    return Response(data={'status': 'ok'}, headers=headers)


@api_view(['get', 'patch'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly, custom_permission.UserIsOwnerOrReadOnly,))
def user_detail(request, username=None):
    data = {}

    try:
        if username is None:
            user = Profile.objects.get(user__username=request.user.username)
        else:
            user = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist as e:
        return Response(data={'message': 'user not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ProfileSerializer(user)
        return Response(data=serializer.data)
    elif request.method == 'PATCH':
        bio = request.data.get('bio', None)
        display_name = request.data.get('display_name', None)
        req_data = (bio, display_name)

        if any(v is not None for v in req_data):
            serializer = serializers.ProfileSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'message': 'update profile successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'bio or display_name needed.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
