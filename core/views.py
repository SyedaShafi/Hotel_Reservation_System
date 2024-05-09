from django.shortcuts import render
from hotels.models import Reviews

# Create your views here.

def home(request):
    reviews = Reviews.objects.all()
    return render(request, 'home.html', {'reviews': reviews})


