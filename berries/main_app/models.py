from django.db import models
from django.urls import reverse

# Create your models here.

class Berry(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    season = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('berry-detail', kwargs={'berry_id': self.id})
    