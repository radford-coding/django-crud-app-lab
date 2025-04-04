from re import M
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from localflavor.us.models import USStateField


# Create your models here.

class Berry(models.Model):
    BERRY_CHOICES = {
        'BLACKBERRY': 'Blackberry',
        'BLUEBERRY': 'Blueberry',
        'CURRANT': 'Currant',
        'ELDERFLOWER': 'Elderflower',
        'GOJI': 'Goji',
        'GOOSEBERRY': 'Gooseberry',
        'MULBERRY': 'Mulberry',
        'RASPBERRY': 'Raspberry',
        'STRAWBERRY': 'Strawberry',
    }
    name = models.CharField(
        max_length=20,
        choices=BERRY_CHOICES,
        default=BERRY_CHOICES['STRAWBERRY'])
    variety = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    season = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_name_display()} ({self.id})'

    def get_absolute_url(self):
        return reverse('berry-detail', kwargs={'berry_id': self.id})


class Picking(models.Model):
    date = models.DateField('Date picked')
    haul = models.DecimalField(max_digits=4, decimal_places=2)
    berry = models.ForeignKey(Berry, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.haul}lbs on {self.date}'
    
    class Meta:
        ordering = ['-date']

class Farm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    city = models.CharField(max_length=50)
    state = USStateField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('farm-detail', kwargs={'pk': self.id})
    