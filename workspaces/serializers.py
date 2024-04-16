from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Workspace


class WorkspaceSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Workspace model."""

    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault(), write_only=True
    # )

    class Meta:
        model = Workspace
        fields = ["id", "user", "title", "body", "created_on", "updated_on"]


class WorkspacesListSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Workspace model list summary."""

    class Meta:
        model = Workspace
        fields = ["id", "user", "title", "updated_on"]
