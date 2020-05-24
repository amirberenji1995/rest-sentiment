from django.db import models

class Sentence(models.Model):
    sen = models.CharField(max_length=300)
