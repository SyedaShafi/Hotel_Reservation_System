# Generated by Django 5.0.3 on 2024-05-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_reviews_user_alter_hotels_image_alter_reviews_hotel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
