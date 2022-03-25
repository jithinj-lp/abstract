from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={'unique': "A user with that username already exists."})

    EMAIL_FIELD = 'username'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"