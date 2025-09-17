from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Bidding, Product
from .models import Review
from django.db.models import Max
from django.contrib.auth.decorators import login_required


# Create your views here.
def product_list(request):
    product = Product.objects.all()
    return render(request, "product_list.html", {"product": product})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.all()  # 🔹 related_name="reviews" hai Review model me
    # highest_bid = product.bids.aggregate(Max("bid_amount"))["bid_amount__max"]
    bids = product.bids.all()  # 🔹 related_name="bidding" hai Bidding model me
    return render(request, "product/product_detail.html", {
        "product": product,
        "reviews": reviews,
        "bids": bids,
    })
 



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
            image=request.FILES.get('image'),
            image1=request.FILES.get('image1'),
            image2=request.FILES.get('image2'),
            image3=request.FILES.get('image3'),
            image4=request.FILES.get('image4')
        )
        return redirect('ecome')

    return render(request, "product/add_product.html")

@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
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
            product.image1 = image1
            product.image2 = image2
            product.image3 = image3
            product.image4= image4

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


@login_required
def add_review(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        name = request.POST.get("name", "")  # 🔹 name field get karo
        comment = request.POST.get("comment", "")
        rating = request.POST.get("rating", 1)

        Review.objects.create(
            user=request.user,
            product=product,
            name=name,  # 🔹 yaha bhi save karo
            comment=comment,
            rating=rating,
        )
        return redirect("product_detail", id=id)

    return render(request, "product/add_review.html", {"product": product})

@login_required
def add_bid(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        amount = request.POST.get("amount", 0)

        Bidding.objects.create(
            user=request.user,
            product=product,
            amount=amount,
        )
        return redirect("product_detail", id=id)

    return render(request, "product/add_bid.html", {"product": product})
