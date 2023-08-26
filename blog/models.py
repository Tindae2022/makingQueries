from django.db import models

# Create your models here.

from datetime import date

class Author(models.Model):
    name = models.Charfield()
    email = models.EmailField()

