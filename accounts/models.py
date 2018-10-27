from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(AbstractUser):
    class Meta:
        db_table = 'user_manager'

    user_id = models.AutoField(
        primary_key=True,
        unique=True,
    )

    username = models.CharField(
        max_length=255,
        unique=True,
    )
    password = models.CharField(
        max_length=255,
    )
    email = models.EmailField(
        unique=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return str(self.username)
