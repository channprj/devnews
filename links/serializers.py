# django
from django.contrib.auth import get_user_model

# third-party
from rest_framework import serializers

# models
from . import models


UserModel = get_user_model()


class TagSerializerField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return data.values_list('name', flat=True)


class LinkSerializer(serializers.ModelSerializer):
    tags = TagSerializerField()

    class Meta:
        model = models.Link
        fields = (
            'url',
            'root_url',
            'title',
            'content',
            'tags',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(LinkSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance
