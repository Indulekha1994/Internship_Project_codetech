from django.db import models

class WebsiteUsage(models.Model):
    website = models.CharField(max_length=255)
    time_spent = models.IntegerField()  # seconds
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.website
