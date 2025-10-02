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
# Details
    brand = models.CharField(("Brand"),max_length=100)
    price = models.FloatField(("Price"), max_length=100)
    discount = models.IntegerField(("Discount"))
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(("Description"))
    is_bidding_open = models.BooleanField(default=True)

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



class Bidding(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.user.username} bid {self.amount} on {self.product.name}"

        # class Auction(models.Model):
        #     product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="auction")
        #     start_time = models.DateTimeField()
        #     end_time = models.DateTimeField()
        #     starting_price = models.FloatField()
        #     is_active = models.BooleanField(default=True)

        #     def __str__(self):
        #         return f"Auction for {self.product.name} ({'Active' if self.is_active else 'Ended'})"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
         return f"{self.user.username} like {self.product.name}"
    class Meta:
        unique_together = ('user', 'product') 
