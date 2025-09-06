from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product


# Create your views here.
def product_list(request):
    product = Product.objects.all()
    return render(request, "product_list.html", {"product": product})

def product_detail(request, id):
    product = get_object_or_404(Product,id=id)
    return render(request, "product/product_detail.html", {"product": product})