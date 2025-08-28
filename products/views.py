from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Products

@login_required
def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.FILES.get("image")

        # 👇 product user ke sath save hoga
        product = Products(
            name=name,
            description=description,
            price=price,
            image=image,
            user=request.user   # logged-in user
        )
        product.save()
