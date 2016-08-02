from django.db import models

#This model is for an individual festival. It will have a one-to-many relationship with Families
#It will act as the sole truth for all info on that festival, any Family will inherit the information from it

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    logo = models.ImageField(default='', blank=True)
    twitter = models.URLField(default='', blank=True)
    facebook = models.URLField(default='', blank=True)
    snapchat = models.URLField(default='', blank=True)
    faq_site = models.URLField(default='', blank=True)
    homepage = models.URLField(default='', blank=True)
    registration_site = models.URLField()

    def __str__(self):
        return self.name
