from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error("username", "Invalid Login")
    else:
        form = LoginForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


# Logout user
def logout_view(request):
    logout(request)
    return redirect("login")


# Signup
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # data is stored in a dictionary for retrevial
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            if password == password_confirmation:
                # create a new login and save info to properties
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                # login user
                login(request, user)
                # redirect to home page
                return redirect("list_projects")
            else:
                form.add_error("password", "Password do not match")
    else:
        form = SignupForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
