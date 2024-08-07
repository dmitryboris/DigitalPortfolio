# Generated by Django 5.0.3 on 2024-05-04 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievements',
            name='user_id',
        ),
        migrations.AddField(
            model_name='achievements',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='achievements',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
