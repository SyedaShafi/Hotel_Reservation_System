# Generated by Django 5.0.3 on 2024-05-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_reservations_hotel_alter_reservations_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='package',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default=0, max_length=30),
        ),
    ]
