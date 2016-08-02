from django.db import models

#This model is for an individual festival. It will have a one-to-many relationship with Families
#It will act as the sole truth for all info on that festival, any Family will inherit the information from it

class Event(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    registration_site = models.URLField()

    def __str__(self):
        return self.name
