from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

from .forms import SigninForm, SignupForm
from .models import UserPTT, Address

def index(request):
    context = {}
    if request.user.is_authenticated:
        context["user"] = request.user

    return render(request, "index.html", context)

def signup(request):
    context = {}
    context["form"] = SignupForm

    if request.method == "POST":
        password = request.POST["password"]
        password_conf = request.POST["password_conf"]

        if password == password_conf:
            address = Address(
                country=request.POST["country"],
                state=request.POST["state"],
                city=request.POST["city"],
                street=request.POST["street"],
                number=request.POST["number"],
                zipcode=request.POST["zipcode"],
            )
            if "complement" in request.POST.keys():
                address.complement = request.POST["complement"]

            address.full_clean()
            address.save()
            try:
                user = UserPTT(
                    name=request.POST["name"],
                    email=request.POST["email"],
                    cpf=request.POST["cpf"],
                    pis=request.POST["pis"],
                    password=request.POST["password"],
                    address=address
                )
                user.full_clean()
                user.save()
                return redirect("/signin/")
                
            except IntegrityError:
                context["message"] = "User already exists."
        else:
            context["message"] = "Passwords do not match"

    return render(request, "signup.html", context)

def signin(request):
    context = {}
    context["form"] = SigninForm

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            context["user"] = user
            return redirect("/")
        else:
            context["message"] = "Invalid Credentials, please try again."

    return render(request, "signin.html", context)

def signout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect("/")
