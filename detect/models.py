from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Use(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
