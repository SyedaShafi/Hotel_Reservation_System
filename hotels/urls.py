from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AllHotels, name='all_hotels' ),
    path('edit_review/<int:id>', views.edit_review, name='edit_review' ),
    path('delete_review/<int:id>', views.delete_review, name='delete_review' ),
    path('detail/<int:id>', views.HotelDetailView.as_view(), name='hotel_details' ),
]
