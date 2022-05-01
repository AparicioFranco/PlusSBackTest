from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    description = models.CharField(max_length=3000)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
