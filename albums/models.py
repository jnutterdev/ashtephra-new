from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    sku = models.CharField(max_length=20)
    image_url = models.ImageField
    release_date = models.DateField

    def __str__(self):
        return f'{self.title} by {self.artist}'