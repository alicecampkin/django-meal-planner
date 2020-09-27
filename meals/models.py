from django.db import models
from core.models import Member


class Meal(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    members = models.ManyToManyField(Member)

    def __str__(self):
        return '%s' % self.name
