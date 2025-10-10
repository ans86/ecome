from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product


def ecome(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'ecome.html', context)

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def check(request):
    return render(request, 'check.html')

# While Loop
# def counter(request):
#     numbers = []
#     count = 0
#     while count < 5:
#         numbers.append(count)
#         count += 1
#     return render(request, "counter.html", {"numbers": numbers})
