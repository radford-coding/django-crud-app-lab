# Generated by Django 5.2 on 2025-04-04 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_farm_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='berry',
            name='farms',
            field=models.ManyToManyField(to='main_app.farm'),
        ),
    ]
