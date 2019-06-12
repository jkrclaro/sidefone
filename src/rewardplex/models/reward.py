from django.db import models


class RewardManager(models.Manager):
    pass


class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='rewards')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RewardManager()