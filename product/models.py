from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(("Name"), max_length=100)
    image = models.ImageField(("Image"), upload_to='product_images/')
    brand = models.CharField(("Brand"),max_length=100)
    price = models.FloatField(("Price"), max_length=100)
    discount = models.IntegerField(("Discount"))
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(("Description"))

    def __str__(self):
        return f"{self.name}"

    