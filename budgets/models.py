from django.db import models
from django.utils.translation import gettext as _

class Budget(models.Model):
    class Category(models.TextChoices):
        home = _("Home")
        car = _("Car")
        taxes = _("Taxes")
        food = _("Food")
        others = _("Others")

    category = models.CharField(max_length=50,choices = Category.choices,default = Category.others)
    income = models.PositiveIntegerField()
    expenses = models.PositiveIntegerField()
