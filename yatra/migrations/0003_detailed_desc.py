# Generated by Django 3.0.4 on 2020-03-27 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yatra', '0002_destination_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailed_desc',
            fields=[
                ('dest_id', models.IntegerField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=20)),
                ('days', models.IntegerField(default=5)),
                ('price', models.IntegerField(default=20000)),
                ('rating', models.IntegerField(default=5)),
                ('dest_name', models.CharField(max_length=25)),
                ('img1', models.ImageField(upload_to='pics')),
                ('img2', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('day1', models.CharField(max_length=100)),
                ('day2', models.CharField(max_length=100)),
                ('day3', models.CharField(max_length=100)),
                ('day4', models.CharField(max_length=100)),
                ('day5', models.CharField(max_length=100)),
                ('day6', models.CharField(max_length=100)),
            ],
        ),
    ]
