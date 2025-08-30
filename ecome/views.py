from django.http import HttpResponse
from django.shortcuts import render
from products.models import Laptop, Car,Anime


def ecome(request):
    laptops = Laptop.objects.all()
    cars = Car.objects.all()
    animes = Anime.objects.all()

    return render(request, "ecome.html", {
        "laptops": laptops,
        "cars": cars,
        "animes": animes,
    })

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def check(request):
    return render(request, 'check.html')