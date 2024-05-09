from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  SetPasswordForm, PasswordChangeForm
from . models import UserAccounts
from reservations.models import Reservations
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/accounts/activate/{uid}/{token}"

            email_subject = "Confirm Your Email"
            email_body = render_to_string('accounts/confirmation_email.html', {'confirm_link' : confirm_link})

            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            messages.success(request, 'Check your email for confirmation!')
            return redirect('register')  
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk = uid)
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account Activated. Please Login.')
        return redirect('login')
    else:
        return redirect('register')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful!')
                return redirect('profile')
            else:
                messages.warning(request, "Invalid username or password.")
    else:
        form = UserLoginForm()        
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'User Logout Successfully.')
    return redirect('homepage')


@login_required
def profile(request):
    user = UserAccounts.objects.get(user=request.user)
    reservations = Reservations.objects.filter(user=user)
    if user:
        balance = user.balance
    else: balance = None

    if not reservations:
        reservations = None

    return render(request, 'accounts/profile.html', {'balance': balance , 'reservations': reservations})




def password_change(request):
    if not request.user.is_authenticated:
        return redirect('register')
    
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            messages.warning(request, 'Password Changed Successfully')
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profile') 
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'accounts/password_change.html', {'form': form})



def set_password(request):
    if not request.user.is_authenticated:
        return redirect('register')
    
    if request.method == 'POST':
        form = SetPasswordForm(user = request.user, data = request.POST)
        if form.is_valid():
            messages.warning(request, 'Password Set Successfully')
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user = request.user)
    return render(request, 'accounts/set_password.html', {'form': form})

@login_required
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservations, pk=id)
    if reservation.user.user != request.user:
        print("user does not match")
        return redirect('profile') 

    if request.method == 'POST':
        reservation.delete()
    return redirect('profile')  
