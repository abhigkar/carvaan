from django.db import models

# Create your models here.
class Song(models.Model):
    cover_art = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    movie = models.CharField(max_length=100)
    artiste = models.CharField(max_length=100)

    def __str__(self):
        return self.title
