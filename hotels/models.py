from django.db import models
from accounts.models import UserAccounts
# Create your models here.

class Hotels(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title




class Rooms(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    description = models.TextField()
    per_day_price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.hotel.title


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Reviews(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)
    
    def __str__(self):
        return self.hotel.title






