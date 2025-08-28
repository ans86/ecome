from django.shortcuts import render, redirect
from .models import CustomUser   # apna model import karo
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password != password_confirm:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("register")

        # user create
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")  # baad me login page bana lena

    return render(request, "register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("ecome")  # apni home page ka url name use karo
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")