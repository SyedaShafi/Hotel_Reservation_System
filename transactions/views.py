from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, View
from .models import Transaction
from .forms import DepositForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.
def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
            'balance': user.useraccounts.balance,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()



class DepositMoneyView(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    form_class = DepositForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.useraccounts
        })
        return kwargs

    def form_valid(self, form): 
        amount = form.cleaned_data.get('amount')
        account = self.request.user.useraccounts
        account.balance += amount 
        # Transaction(account=account, amount=amount)
        #  here i am creating the instance of transactions model with user and amount
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}TK is deposited to your account successfully. Check Email.'
        )
        send_transaction_email(self.request.user, amount, "Deposite Message", "transactions/deposit_email.html")
        return super().form_valid(form)