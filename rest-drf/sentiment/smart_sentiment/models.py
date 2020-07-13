from django.db import models

class Page(models.Model):
    link = models.URLField(max_length = 250)
