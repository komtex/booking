from django.db import models
import datetime

class Hotel(models.Model):
    city = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    room = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.city} hotel- {self.name}, room- {self.room}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    hotels = models.ManyToManyField(Hotel, blank=True, related_name="passengers")
    def __str__(self):
        return f"{self.first} {self.last}"

class Comment(models.Model):
    commenter = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="writer")
    content = models.CharField(max_length=240, blank=True)
    time_posted = models.DateTimeField(auto_now_add=True)
    hotels_liked = models.ManyToManyField(Hotel, blank=True, related_name="liked_writer")

    def __str__(self):
        return f"{self.commenter} on {self.commenter.inn}"
"""
    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "content": self.content,
            "time_posted": self.timestamp.strftime("%b %-d %Y, %-I:%M %p"),
            "likes": self.likes
        }
"""
