from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings  # Ensure settings is imported

import os

print("MEDIA_ROOT:", settings.MEDIA_ROOT)

@login_required(login_url="/accounts/login/")  # Redirects unauthenticated users
def home(request):
    return render(request, "registration/home.html")  # Render the home page

def menu_categories(request):
    return render(request, "registration/Menu-categories.html")  # Render menu categories

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after successful signup
            return redirect("login")
    else:
        form = UserCreationForm()  # Initialize form for GET request

    return render(request, "registration/signup.html", {"form": form})  # Render signup page



