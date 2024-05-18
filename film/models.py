from django.db import models

class Film(models.Model):
    name = models.CharField(default= 'film_name',max_length=250)
    director = models.CharField(default= 'some director',max_length=250)
    release_year = models.IntegerField()

    def __str__(self):
        return self.name
