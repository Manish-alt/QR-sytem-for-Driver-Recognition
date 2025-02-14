from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import OfficerProfile

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            current_user = OfficerProfile.objects.get(user__id=request.user.id)
            messages.success(request, ('You have been logged in'))
            return redirect('home')
        else:
            messages.success("There was an error logging in. Please try again")
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('home')

# def driverProfile(request, pk):
#     if request.user.is_authenticated:
#         driver
#     return render(request, 'driver_profile.html', {})
            
