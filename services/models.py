from django.db import models

# Create your models here.
"""This Model creates a model called Service that gives data fields that include text,images and numbers."""


class Service(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
