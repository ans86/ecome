from django.db import models
from django.conf import settings

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products_images/')
    cpu = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 👈 yahan add kiya

    def __str__(self):
        return f"{self.name} - {self.user.username}"
    

class Car(models.Model):
     name = models.CharField(max_length=255)
     image = models.ImageField(upload_to="cars/")
     model = models.CharField(max_length=100)
     engine = models.CharField(max_length=100)
     enginepower = models.CharField(max_length=100)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     madein = models.CharField(max_length=100)
     topspeed = models.CharField(max_length=100)
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

     def __str__(self):
        return f"{self.name}- {self.user.username}"
     

class Anime(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='anime_images/')
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.title}- {self.user.username}"