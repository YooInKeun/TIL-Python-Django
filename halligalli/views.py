from django.shortcuts import render
import time
import random
import json
import time

from .models import Player
from .models import Card

# Create your views here.

com = Player.objects.get(player_name = 'Computer')
user = Player.objects.get(player_name = 'User')
card = Card.objects.get(owner = 'None')

def home(request):

    init_player()

    return render(request, 'home.html')

def play_game(request):

    init_player()

    return render(request, 'play_game.html')

def show_card(request):

    com_num = random.randrange(1,6)
    user_num = random.randrange(1,6)

    json_str = json.dumps(card.card_info)
    json_data = json.loads(json_str)
    
    com.current_card = json_data[str(com_num)]
    user.current_card = json_data[str(user_num)]

    time.sleep(2)

    return render(request, 'play_game.html', {'com' : com, 'user' : user})

def init_player():

    com.player_name = 'Computer'
    com.comment = 'None'
    com.card_num = 6
    com.score = 0
    com.current_card='None'
    com.bell_flag=0

    user.player_name = 'User'
    user.userment = 'None'
    user.card_num = 6
    user.score = 0
    user.current_card='None'
    user.bell_flag=0

