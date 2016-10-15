from django.db import models

#This model is for an individual festival. It will have a one-to-many relationship with Families
#It will act as the sole truth for all info on that festival, any Family will inherit the information from it

class Event(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=60, editable=False)
    description = models.TextField(default='', blank=True)
    cover_photo = models.ImageField(default='', blank=True, upload_to='media/')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    logo = models.ImageField(default='', blank=True)
    #social URLs
    twitter = models.URLField(default='', blank=True)
    facebook = models.URLField(default='', blank=True)
    snapchat = models.URLField(default='', blank=True)
    instagram = models.URLField(default='', blank=True)
    youtube = models.URLField(default='', blank=True)
    #app URLs
    ios_app = models.URLField(default='', blank=True)
    android_app = models.URLField(default='', blank=True)
    #Important URLs
    faq_site = models.URLField(default='', blank=True)
    homepage = models.URLField(default='', blank=True)
    registration_site = models.URLField(default='', blank=True)
    parking_pass = models.URLField(default='', blank=True)
    venue_map = models.URLField(default='', blank=True)
    #email
    email = models.EmailField(max_length=254, default='')

    def __str__(self):
        return self.name

class Restrictions(models.Model):
    #common questionable items
    event =  models.OneToOneField(Event, related_name="event_restrictions")
    totems = models.BooleanField(default='')
    hydration_pack = models.BooleanField(default='')
    camping_stove = models.BooleanField(default='')
    beer = models.BooleanField(default='')
    wine = models.BooleanField(default='')
    liqour = models.BooleanField(default='')
    alcohol_policy = models.TextField(default='', blank=True)
