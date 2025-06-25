from django.db import models
from cloudinary.models import CloudinaryField


class Car(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    kilometers = models.PositiveIntegerField()
    image = CloudinaryField('image')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Autopart(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return f"{self.name} - {self.brand}"
