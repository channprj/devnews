# django
from django.contrib.auth import get_user_model

# third-party
from rest_framework import serializers

# models
from . import models


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'username',
            'is_active',
        )
        read_only_fields = (
            'username',
            'is_active',
        )


class ProfileSerializer(serializers.Serializer):
    user = UserSerializer(required=False)  # May be an anonymous user.
    display_name = serializers.CharField(max_length=30)
    bio = serializers.CharField(max_length=1000)
    karma = serializers.FloatField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = models.Profile
        fields = ('bio', 'display_name')

    def update(self, instance, validated_data):
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.bio = validated_data.get('bio', instance.bio)
        # instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
