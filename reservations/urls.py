from django.urls import path
from . import views
urlpatterns = [
    path('add/<str:id>/', views.ReservationsView.as_view(), name="reservations"),
]
