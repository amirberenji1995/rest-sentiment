from django.db import models

class Movie(models.Model):
    link = models.URLField(max_length = 250)
