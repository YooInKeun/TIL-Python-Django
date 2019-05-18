from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'home.html')

def play_game(request):

    return render(request, 'play_game.html')