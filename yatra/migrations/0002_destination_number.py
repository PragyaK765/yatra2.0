# Generated by Django 3.0.4 on 2020-03-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yatra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='number',
            field=models.IntegerField(default=2),
        ),
    ]
