from django.db import models

class Product(models.Model):
    link = models.URLField(max_length = 250)
