from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import random
import time

# Create your views here.

def home(request):

    value = random.randrange(1,7)
    print(value)

    for i in range(1, 4):

        print(4-i)
        print("초 후에 게임을 시작합니다")

        time.sleep(1)

    return render(request, 'home.html', {'value' : value})

def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    return render(request, 'login.html')