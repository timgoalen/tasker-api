from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the User model."""

    class Meta:
        model = User
        fields = ["url", "email"]
        # fields = ["url", "username", "email"]
