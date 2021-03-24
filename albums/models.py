from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    label = models.CharField(max_length=100)
    sku = models.CharField(max_length=20)
    image_url = models.ImageField
    release_date = models.DateField

    def __str__(self):
        return self.title
        return self.artist