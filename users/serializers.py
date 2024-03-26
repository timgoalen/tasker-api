# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     """Serializer for the User model."""

#     class Meta:
#         model = User
#         fields = ["url", "email"]
# fields = ["url", "username", "email"]


class MyUserSerializer(serializers.ModelSerializer):
# class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the User model."""

    class Meta:
        model = get_user_model()
        fields = ("id", "email", "first_name", "last_name")
