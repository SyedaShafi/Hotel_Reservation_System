from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse_lazy
from hotels.models import Rooms
from django.contrib import messages
from transactions.models import Transaction
from . models import Reservations
from . forms import ReservationsForm
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


class ReservationsView(LoginRequiredMixin, View):
    template_name = 'reservations/reservation_form.html'
    form_class = ReservationsForm
    model = Reservations
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'    

    def get(self, request, *args, **kwargs):
        room_id = kwargs.get(self.pk_url_kwarg)
        room = Rooms.objects.filter(id=room_id).first()
        if not room:
            return redirect('homepage')  
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        room_id = kwargs.get(self.pk_url_kwarg)
        room = Rooms.objects.filter(id=room_id).first()
        form = self.form_class(request.POST)
        if form.is_valid():
            package = form.cleaned_data['package']
            price = room.per_day_price * int(package)
            account = request.user.useraccounts
            if account.balance < price:
                messages.warning(request, 'You do not have sufficient balance')
                return redirect('hotel_details', id=room.hotel.id)
            account.balance -= price
            transaction = Transaction.objects.create(account=account, amount=price)
            Reservations.objects.create(user=account, hotel=room.hotel, room =  room,package=package, transaction=transaction)
            account.save(update_fields=['balance'])
            messages.success(request, f'You made a reservation for {package} days with {"{:,.2f}".format(float(price))} tk. Check email')

            send_transaction_email(request.user, price, "Reservations Message", "reservations/reservations_email.html")

            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})