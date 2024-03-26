from django.db import models
from django.contrib.auth.models import User
from users.models import MyUser


class Workspace(models.Model):
    """
    MODEL: database for Wokespace objects.
    """

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="workspaces")
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.text
