from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                profile = request.user.profile
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email = request.POST['email'])
                name = request.POST['name']
                phone = request.POST['phone']
                region_sido = request.POST['sido']
                region_sigungu = request.POST['gungu']
                profile = Profile(user = user, name = name, phone = phone, region_sido = region_sido, region_sigungu = region_sigungu, profile_pic = request.FILES['profile_pic'])
                profile.save()
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')