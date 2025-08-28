from django.http import HttpResponse
from django.shortcuts import render



def ecome(request):
    from products.models import Products
    products = Products.objects.all()
    return render(request, "ecome.html", {"products": products})


def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def check(request):
    return render(request, 'check.html')