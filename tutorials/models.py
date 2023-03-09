from django.db import models


class User(models.Model):
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    type = models.BooleanField(default=False)

class Tutorial(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return self.name