from django.db import models
from django.conf import settings

class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 👈 yahan add kiya

    def __str__(self):
        return f"{self.name} - {self.user.username}"