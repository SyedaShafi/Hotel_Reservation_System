from django.contrib import admin
from .models import Hotels, Reviews, Rooms
# Register your models here.
admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(Reviews)