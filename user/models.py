from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=150, blank=True, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=150, blank=True, validators=[MinLengthValidator(2)])
    email = models.EmailField(
        max_length=70,
        unique=True,
        validators=[MinLengthValidator(2)],
        error_messages={
            'unique': "A user with that email already exists.",
        },
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


class Phone(models.Model):
    number = models.IntegerField(null=True, blank=True)
    area_code = models.IntegerField(null=True, blank=True)
    country_code = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='phones')
