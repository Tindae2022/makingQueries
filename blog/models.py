from django.db import models

# Create your models here.

from datetime import date


class Bolg(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.Charfield()
    email = models.EmailField()

    def __str__(self):
        return self.name

