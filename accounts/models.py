from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class UserAccounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100, choices = GENDER_TYPE)
    account_no = models.IntegerField(unique=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return self.user.username