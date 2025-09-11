from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
def product_list(request):
    product = Product.objects.all()
    return render(request, "product_list.html", {"product": product})

def product_detail(request, id):
    product = get_object_or_404(Product,id=id)
    return render(request, "product/product_detail.html", {"product": product})



def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            user=request.user,
            name=request.POST['name'],
            brand=request.POST.get('brand', ''),
            price=request.POST['price'],
            discount=request.POST.get('discount', 0),
            stock=request.POST.get('stock', 0),
            description=request.POST.get('description', ''),
            image=request.FILES.get('image')
        )
        return redirect('ecome')

    return render(request, "product/add_product.html")

@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        stock = request.POST.get('stock')
        description = request.POST['description']

        if not name or not brand or not price or not discount or not stock or not description:
            return render(request, 'edit_product.html', {
                'product': product,
                'error': 'Please fill in all fields.'
            })

        product.name = name
        product.brand = brand
        product.price = price
        product.discount = discount
        product.stock = stock
        product.description = description

        if image:
            product.image = image

        product.save()
        return redirect('my_list')

    return render(request, 'product/edit_product.html', {'product': product})

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('my_list')

@login_required
def my_list(request):
    products = Product.objects.filter(user=request.user)
    return render(request, "my_list.html", {"products": products})
