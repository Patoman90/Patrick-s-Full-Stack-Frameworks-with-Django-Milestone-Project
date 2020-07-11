from django.db import models

# Create your models here.
"""This Model creates a model called Reviews that gives data fields that include text and images"""


class Reviews(models.Model):
    Product = models.CharField(max_length=200, default='')
    Review = models.TextField()

    def __str__(self):
        return self.name
