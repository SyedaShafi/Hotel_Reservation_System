# Generated by Django 5.0.3 on 2024-05-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_reservations_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='package',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default=0, max_length=30),
        ),
    ]