from django.db import models
from accounts.models import UserAccounts
from hotels.models import Rooms, Hotels
from transactions.models import Transaction
# Create your models here.
PACKAGE_TYEP = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)
class Reservations(models.Model):
    user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, blank=True, null=True)
    hotel =  models.ForeignKey(Hotels, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    package = models.CharField(choices=PACKAGE_TYEP, max_length=30, default=0)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.user.first_name} {self.user.user.last_name} - Hotel: {self.hotel.title}"