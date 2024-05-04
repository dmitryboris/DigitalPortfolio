# Generated by Django 5.0.3 on 2024-05-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('user_id', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date of publication')),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Achievement',
                'verbose_name_plural': 'Achievements',
            },
        ),
    ]
