from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=6,
        choices=[('MALE','ERKEK'),('FEMALE','KADIN')]
    )
    phone = models.CharField(blank=True, max_length=15)
    address = models.CharField(blank=True, max_length=150)


    def __srt__(self):
        return self.user.username
