from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=20)
    due = models.DateTimeField()
    brief = models.TextField(max_length=200)
    site = models.CharField(max_length=50, blank=True)
    user = models.ManyToManyField(
        User,
        through='Signup',
        through_fields=('activity', 'user'),
    )

    def __str__(self):
        s = self.name
        return s


class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    achieve = models.BooleanField(default=False)
    duty = models.CharField(max_length=20, blank=True)

    def __str__(self):
        s = self.activity.name + ': ' + str(self.user) + ' - ' + str(self.achieve)
        return s

