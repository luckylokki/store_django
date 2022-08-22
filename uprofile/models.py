from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserModel(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, null=True)
    city = models.CharField(max_length=32, blank=True)

    class Meta:
        db_table = "auth_user"
        verbose_name = "user"
        verbose_name_plural = "users"
