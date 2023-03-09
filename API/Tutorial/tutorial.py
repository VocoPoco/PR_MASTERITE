from django.db import models

class Tutorial(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return self.name