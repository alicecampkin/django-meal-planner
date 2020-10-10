from django.db import models
from accounts.models import User
# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='uploads/members/', default='/icons/member.svg')

    def __str__(self):
        return '%s Household | %s' % (self.user, self.name)
