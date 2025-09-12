from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(("Name"), max_length=100)
    image = models.ImageField(("Image"), upload_to='product_images/')
 # Extra images
    image1 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product_images/', null=True, blank=True)


    brand = models.CharField(("Brand"),max_length=100)
    price = models.FloatField(("Price"), max_length=100)
    discount = models.IntegerField(("Discount"))
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(("Description"))

    def __str__(self):
        return f"{self.name}"

    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=1)  # 1–5 stars
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name} - {self.product.name} - ({self.rating}⭐) "    