from django.contrib import admin
from .models import Hotel, Passenger, Comment
class HotelAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "name", "room")
    
admin.site.register(Hotel)
admin.site.register(Passenger)
admin.site.register(Comment)
