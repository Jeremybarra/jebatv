# Generated by Django 2.0.1 on 2018-01-13 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='serie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='series.Serie'),
            preserve_default=False,
        ),
    ]
