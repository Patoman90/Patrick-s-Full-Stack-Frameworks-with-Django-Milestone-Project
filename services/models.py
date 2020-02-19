from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places='2')

    def __str__(self):
        return self.name
