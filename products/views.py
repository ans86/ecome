from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from products.models import Laptop, Car, Anime


@login_required
def add_laptop(request):
    if request.method == "POST":
        name = request.POST.get("name")
        cpu = request.POST.get("cpu")
        ram = request.POST.get("ram")
        price = request.POST.get("price")
        image = request.FILES.get("image")
        about = request.POST.get("about")

        # 👇 laptop user ke sath save hoga
        laptop = Laptop(
            name=name,
            cpu=cpu,
            ram=ram,
            price=price,
            image=image,
            about=about,
            user=request.user   # logged-in user
        )
        laptop.save()


def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    return render(request, "laptop_detail.html", {"laptop": laptop})

def user_logout(request):
    logout(request)
    return redirect("ecome")



def car(request):
    if request.method=="POST":
        name = request.POST['name']
        image = request.FILES.get('image')
        model = request.POST['model']
        engine = request.POST['engine']
        enginepower = request.POST['enginepower']
        price = request.POST['price']
        madein = request.POST['madein']
        topspeed = request.POST['topspeed']
        car = Car(name=name, image=image, model=model, engine=engine, enginepower=enginepower, price=price, madein=madein, topspeed=topspeed)
        car.save()



def anime_list(request):
    animes = Anime.objects.all()
    return render(request, "anime_list.html", {"animes": animes})
