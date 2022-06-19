from django.contrib.auth.models import AbstractUser
# from jobs.models import Job
from django.db import models


class User(AbstractUser):
    date_of_birth = models.DateField('date_of_birth', null=True)
