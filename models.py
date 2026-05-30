from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.room_name
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender}: {self.message[:20]}" 
    

