from django.db import models

# Create your models here.

class Berry(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    season = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'