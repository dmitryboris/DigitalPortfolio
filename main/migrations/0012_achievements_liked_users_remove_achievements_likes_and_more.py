# Generated by Django 5.0.3 on 2024-06-11 12:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_merge_20240611_1710'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_achievements', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='achievements',
            name='likes',
        ),
        migrations.AddField(
            model_name='achievements',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]