from pyexpat.errors import messages
from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product, Bidding, Like, Category, Cart
from .models import Review
from django.db.models import Max
from django.contrib.auth.decorators import login_required



def search(request):
    query = request.GET.get("q")
    category = request.GET.get("category")
    
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)
        return render(request, "product/search_results.html", {"products": products, "query": query})



def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'product/category_products.html', {
        'category': category,
        'products': products
    })


def product_list(request):
    product = Product.objects.all()
    return render(request, "product_list.html", {"product": product})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    highest_bid = product.bids.aggregate(Max("amount"))["amount__max"]
    reviews = product.reviews.all()
    bids = product.bids.all().order_by('-amount')

    liked = False
    in_cart = False

    if request.user.is_authenticated:
        liked = Like.objects.filter(user=request.user, product=product).exists()
        in_cart = Cart.objects.filter(user=request.user, product=product).exists()

    return render(request, "product/product_detail.html", {
        "product": product,
        "reviews": reviews,
        "bids": bids,
        "liked": liked,
        "in_cart": in_cart,
        "highest_bid": highest_bid,
    })



def add_product(request):
    categories = Category.objects.all()
    
    if request.method == "POST":
        category_slug = request.POST.get('category')
        category = Category.objects.get(slug=category_slug)

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
            image4=request.FILES.get('image4'),
            category=category
        )
        return redirect('ecome')

    return render(request, "product/add_product.html", {'categories': categories})



@login_required
def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)

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
def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.delete()
    return redirect('my_list')

@login_required
def my_list(request):
    products = Product.objects.filter(user=request.user)
    return render(request, "my_list.html", {"products": products})


@login_required
def add_review(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == "POST":
        name = request.POST.get("name", "")
        comment = request.POST.get("comment", "")
        rating = request.POST.get("rating", 1)

        Review.objects.create(
            user=request.user,
            product=product,
            name=name,
            comment=comment,
            rating=rating,
        )
        return redirect("product_detail", slug=slug)

    return render(request, "product/add_review.html", {"product": product})

@login_required
def add_bid(request, slug):
    product = get_object_or_404(Product, slug=slug)

    existing_bid = Bidding.objects.filter(user=request.user, product=product).first()  
    if existing_bid:
        existing_bid.amount = request.POST.get("amount", 0)
        existing_bid.save()
        return redirect("product_detail", slug=slug)

    if not product.is_bidding_open:
        return redirect("product_detail", slug=slug)


    if request.method == "POST":
        amount = request.POST.get("amount", 0)

        Bidding.objects.create(
            user=request.user,
            product=product,
            amount=amount,
        )
        return redirect("product_detail", slug=slug)

    return render(request, "product/add_bid.html", {"product": product})


# @login_required
# def add_bid(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == "POST":
#         amount = request.POST.get('amount')
#         Bidding.objects.create(product=product, user=request.user, amount=amount)
#         return redirect('product_detail', id=id)
#     return redirect('product_detail', id=id)

# @login_required
# def add_review(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == "POST":
#         comment = request.POST.get('comment')
#         rating = request.POST.get('rating')
#         Review.objects.create(product=product, user=request.user, comment=comment, rating=rating)
#         return redirect('product_detail', id=id)
#     return redirect('product_detail', id=id)





@login_required
def edit_bid(request, id):
    bid = get_object_or_404(Bidding, id=id)

    if request.method == "POST":
        amount = request.POST.get('amount')
        bid.amount = amount

        if not amount:
            return render(request, 'product/edit_bid.html', {
                'bid': bid, 'error': "Please enter a bid amount."
            })

        bid.amount = amount
        bid.save()
        return redirect("product_detail", slug=bid.product.slug)

    return render(request, "product/edit_bid.html", {"bid": bid})


@login_required
def close_bid(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.user != product.user:
        return redirect("product_detail", slug=product.slug)
    product.is_bidding_open = False
    highest_bid = Bidding.objects.filter(product=product).order_by('-amount').first()
    if highest_bid:
        product.winner = highest_bid.user
    product.save()

    return redirect("product_detail", slug=product.slug)


@login_required
def add_like(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    Like.objects.get_or_create(user=request.user, product=product)
    return redirect('liked_products')



@login_required
def liked_products(request):
    likes = Like.objects.filter(user=request.user).select_related('product')
    return render(request, "product/liked_products.html", {"likes": likes})


@login_required
def unlike_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    like = Like.objects.filter(user=request.user, product=product).first()
    if like:
        like.delete()
    return redirect('ecome')


@login_required
def add_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    Cart.objects.get_or_create(user=request.user, product=product)
    return redirect('cart_products')


@login_required
def cart_products(request):
    carts = Cart.objects.filter(user=request.user).select_related('product')
    return render(request, "product/cart_products.html", {"carts": carts})


