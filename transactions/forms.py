from django import forms
from .models import Transaction

class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') 
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.account = self.account
        return super().save()

    def clean_amount(self): 
        min_deposit_amount = 1000
        amount = self.cleaned_data['amount']
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least BDT {min_deposit_amount}'
            )
        return amount
    
  