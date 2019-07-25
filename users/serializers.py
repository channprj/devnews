# django
from django.contrib.auth import get_user_model

# third-party
from rest_framework import serializers

# models
from .models import Profile


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id',
            'username',
            'email',
            'last_login',
        )
        read_only_fields = (
            'last_login',
        )


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = (
            'user',
            'display_name',
            'bio',
            'karma',
            'created_at',
        )
        read_only_fields = (
            'user',
            'karma',
            'created_at',
        )
