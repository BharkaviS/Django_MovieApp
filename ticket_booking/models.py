from django.db import models
from django.utils import timezone
# Create your models here.

class MovieDetails(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.SlugField(unique = True) #Primary key.Even if more than one movie has the same name, then they are reached via slugfield.
    show_timing1 = models.DateTimeField(default = timezone.now)
    show_timing2 = models.DateTimeField(default = timezone.now)
    price =  models.IntegerField()
    Tickets_available = models.IntegerField(default=100)
    Tickets_booked = models.IntegerField(default=0)
    Tickets_totprice = models.IntegerField(default=0)
    image = models.ImageField(upload_to="media/",blank=True)

    def get_absolute_url(self):
        return f"/{self.slug}"  #this is used to refer url mapping for the slug.

    def get_absolute_url(self):
        return f"/{self.slug}/booked"
