# Generated by Django 2.0.1 on 2018-01-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_episode_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='image',
            field=models.FileField(default='/static/series/pictures/placeholder_series.png', upload_to=''),
        ),
    ]