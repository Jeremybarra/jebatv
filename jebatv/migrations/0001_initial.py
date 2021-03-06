# Generated by Django 2.0.1 on 2018-01-13 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('description', models.TextField(default='Aucune description renseignée', verbose_name='Description')),
                ('content', models.FileField(upload_to='')),
            ],
        ),
    ]
