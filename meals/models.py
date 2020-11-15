from django.db import models
from core.models import Member
from accounts.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


class Meal(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    members = models.ManyToManyField(Member)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mealtime = models.CharField(max_length=255, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return '%s' % self.name
