# from django.db import models
from djongo import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_file_size


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    sex = models.CharField(max_length=20, null=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=False)
    list_id_exam = models.TextField(null=True, blank=True)
    school = models.TextField(null=False)
    image = models.ImageField(null=True, blank=True, upload_to='user/logo', validators=[validate_file_size], default='user/logo/user.png')
    list_id_history = models.TextField(null=True, blank=True)
    options = models.JSONField(null=True, blank=True, default=dict)



