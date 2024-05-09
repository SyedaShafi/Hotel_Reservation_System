from django.db import models
from accounts.models import UserAccounts
# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(UserAccounts, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account)
