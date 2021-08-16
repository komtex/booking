from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Hotel, Passenger, Comment
import datetime

def index(request):
    return render(request, "vacation/index.html")

@login_required    
def hotel_view(request):
    return render(request,"vacation/hotels.html", {
    "hotels": Hotel.objects.all()
    })

@login_required
def hotel(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    passengers = hotel.passengers.all()
    non_passengers = Passenger.objects.exclude(hotels=hotel).all()
    return render(request, "vacation/hotel.html", {
    "hotel": hotel,
    "passengers": passengers,
    "non_passengers": non_passengers
    })

@login_required
def book(request, hotel_id):
    #with post request add a new hotel
    if request.method == "POST":
        # accessing the hotel
        hotel = Hotel.objects.get(pk=hotel_id)
        # looking for passenger id from form data
        passenger_id = int(request.POST["passenger"])
        #look for passenger by the # id
        passenger = Passenger.objects.get(pk=passenger_id)
        # add passenger to the hotel
        passenger.hotels.add(hotel)
        #redirect user to the hotel page
        return HttpResponseRedirect(reverse("hotel", args=(hotel.id,)))
