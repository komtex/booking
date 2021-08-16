from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index, name='index'),
    path("<int:hotel_id>", views.hotel, name="hotel"),
    path("<int:hotel_id>/book", views.book, name="book"),
    path("hotels", views.hotel_view, name="hotels")
]
