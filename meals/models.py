from django.db import models
from core.models import Member
from accounts.models import User


class Meal(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    members = models.ManyToManyField(Member)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name
