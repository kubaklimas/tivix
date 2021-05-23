from django.db import models
from django.contrib.auth.models import AbstractUser

from budgets.models import Budget

class User(AbstractUser):
    budgets = models.ManyToManyField(Budget)
    email = models.EmailField(unique=True)