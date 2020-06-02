from django.db import models

class Post(models.Model):
    link = models.URLField(max_length = 250)    
