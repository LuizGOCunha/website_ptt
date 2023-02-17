from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpRequest

from .forms import SigninForm, SignupForm, EditInfoForm
from .models import UserPTT, Address


def index(request: HttpRequest):
    context = {}
    if request.user.is_authenticated:
        context["authenticated"] = True

    return render(request, "index.html", context)


def signup(request: HttpRequest):
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
                    address=address,
                )
                user.full_clean()
                user.save()
                return redirect("/signin/")

            except IntegrityError:
                context["message"] = "User already exists."
        else:
            context["message"] = "Passwords do not match"

    return render(request, "signup.html", context)


def signin(request: HttpRequest):
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


def signout(request: HttpRequest):
    if request.user.is_authenticated:
        print(request.user)
    logout(request)
    return redirect("/")


def editinfo(request: HttpRequest):
    context = {}
    context["form"] = EditInfoForm

    if request.user.is_authenticated:
        if request.method == "POST":
            user = UserPTT.objects.get(id=request.user.id)
            address = Address.objects.get(id=user.address.id)
            if "name" in request.POST.keys():
                if request.POST["name"]:
                    user.name = request.POST["name"]
                    print(user.name)
            if "pis" in request.POST.keys():
                if request.POST["pis"]:
                    user.pis = request.POST["pis"]
                    print(user.pis)
            if "cpf" in request.POST.keys():
                if request.POST["cpf"]:
                    user.cpf = request.POST["cpf"]
                    print(user.cpf)
            if "email" in request.POST.keys():
                if request.POST["email"]:
                    user.email = request.POST["email"]
                    print(user.email)
            if "street" in request.POST.keys():
                if request.POST["street"]:
                    address.street = request.POST["street"]
                    print(address.street)
            if "number" in request.POST.keys():
                if request.POST["number"]:
                    address.number = request.POST["number"]
            if "city" in request.POST.keys():
                if request.POST["city"]:
                    address.city = request.POST["city"]
            if "state" in request.POST.keys():
                if request.POST["state"]:
                    address.state = request.POST["state"]
            if "country" in request.POST.keys():
                if request.POST["country"]:
                    address.country = request.POST["country"]
            if "complement" in request.POST.keys():
                if request.POST["complement"]:
                    address.complement = request.POST["complement"]
            if "zipcode" in request.POST.keys():
                if request.POST["zipcode"]:
                    address.zipcode = request.POST["zipcode"]
            user.full_clean()
            user.save()
            address.full_clean()
            address.save()
            context["message"] = "Changes successful"

    else:
        return redirect("/")

    return render(request, "editinfo.html", context)
