from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name = "register"),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('profile/', views.profile, name = "profile"),
    path('delete_reservation/<int:id>', views.delete_reservation, name = "delete_reservation"),
    path('activate/<uid64>/<token>', views.activate, name = "activate"),
    path('password_change/', views.password_change, name = "password_change"),
    path('set_password/', views.set_password, name = "set_password"),
    
 
]
