# built-in
from datetime import date

# django
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.shortcuts import render

# third-party
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

# utils
from utils import custom_permission

# serializers
from . import serializers

# models
from .models import Link


UserModel = get_user_model()


@permission_classes((permissions.IsAuthenticatedOrReadOnly, custom_permission.IsOwnerOrReadOnly,))
class LinkViewSet(viewsets.ViewSet):
    def list(self, request):
        # queryset = Link.objects.filter(created_at__date=date.today())
        queryset = Link.objects.all()
        serializer = serializers.LinkSerializer(queryset, many=True)
        return Response(serializer.data)
