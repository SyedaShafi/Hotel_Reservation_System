from django.shortcuts import render, redirect, get_object_or_404
from . models import Hotels, Reviews, Rooms
from reservations.models import Reservations
from django.views.generic import DetailView
from . forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
class HotelDetailView(DetailView):
    model = Hotels
    pk_url_kwarg = 'id'
    template_name = 'hotels/hotel_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hotel = self.get_object()
        reviews = Reviews.objects.filter(hotel=hotel)
        rooms = Rooms.objects.filter(hotel=hotel)
        print(rooms[0].image)
        context['review_form'] = CommentForm()
        context['reviews'] = reviews
        context['hotel'] = hotel
        context['rooms'] = rooms
        return context     
       
    def post(self, request, *args, **kwargs):
        review_form = CommentForm(data=self.request.POST)
        hotel = self.get_object()
        user_account = request.user.useraccounts

        if Reservations.objects.filter(user = user_account, hotel = hotel).exists():
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.hotel = hotel
                new_review.user = user_account
                new_review.save()
                messages.success(request, 'Your review has been submitted successfully.')
        else:
           messages.warning(request, 'You must have a reservation at this hotel to leave a review.')
   
        return self.get(request, *args, **kwargs)
    

def AllHotels(request):
    hotels = Hotels.objects.all()
    return render(request,'hotels/all_hotel.html', {'hotels': hotels} )




@login_required
def edit_review(request, id):
    review = get_object_or_404(Reviews, id=id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Review Updated')
            return redirect('hotel_details', id=review.hotel.id)  
    else:
        form = CommentForm(instance=review) 

    return render(request, 'hotels/edit_review.html', {'form': form})



@login_required
def delete_review(request, id):
    review = get_object_or_404(Reviews, id=id)
    if request.user == review.user.user:
        if request.method == 'POST':
            review.delete()
            messages.warning(request, 'Review Deleted!')
            return redirect('hotel_details', id= review.hotel.id) 
    else:
        return redirect('hotel_details', id= review.hotel.id) 