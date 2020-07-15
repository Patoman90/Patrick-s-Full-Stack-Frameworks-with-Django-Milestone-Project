from django.db import models

# Create your models here.
"""This Model creates a model called Product that gives data fields that includes text,images and numbers."""


class Product(models.Model):
    image = models.ImageField(upload_to='images')
    is_service = models.BooleanField()
    name = models.CharField(max_length=200, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
