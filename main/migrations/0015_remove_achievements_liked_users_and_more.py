# Generated by Django 5.0.3 on 2024-06-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_merge_20240613_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievements',
            name='liked_users',
        ),
        migrations.RemoveField(
            model_name='achievements',
            name='views_users',
        ),
        migrations.AddField(
            model_name='achievements',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
