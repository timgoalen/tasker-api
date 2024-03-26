# from django.contrib.auth.models import User
# from rest_framework import permissions, viewsets
from rest_framework import viewsets

# from users.serializers import UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """

#     queryset = User.objects.all().order_by("-date_joined")
#     # queryset = users.MyUser.objects.all().order_by("-date_joined")
#     serializer_class = UserSerializer
#     # permission_classes = [permissions.IsAuthenticated]


# FROM DJANGO-REST-AUTHMAIL EXAMPLE PROJECT:
# https://github.com/celiao/django-rest-authemail/blob/master/example_project/accounts/views.py 

from django.contrib.auth import get_user_model

from django.utils.translation import gettext as _

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import MyUserSerializer
# from users.serializers import MyUserSerializer, MyUserChangeSerializer


# class MyUserMe(APIView):
class MyUserMeViewSet(viewsets.ModelViewSet):
    MyUser = get_user_model()
    # permission_classes = (IsAuthenticated,)
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all().order_by("-date_joined")

    def get(self, request, format=None):
        return Response(self.serializer_class(request.user).data)


# class MyUserMeChange(APIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = MyUserChangeSerializer

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             user = request.user

#             if 'first_name' in serializer.data:
#                 user.first_name = serializer.data['first_name']
#             if 'last_name' in serializer.data:
#                 user.last_name = serializer.data['last_name']
#             if 'date_of_birth' in serializer.data:
#                 user.date_of_birth = serializer.data['date_of_birth']

#             user.save()

#             content = {'success': _('User information changed.')}
#             return Response(content, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)