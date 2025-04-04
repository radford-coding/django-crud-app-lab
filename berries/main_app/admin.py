from django.contrib import admin
from .models import Berry, Picking, Farm

# Register your models here.

admin.site.register(Berry)
admin.site.register(Picking)
admin.site.register(Farm)