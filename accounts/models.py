from django.db import models

# Create your models here.


class quote(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    user_quote = models.TextField(max_length=500, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.full_name, self.date)
