from django.shortcuts import render, redirect
from .models import Yut
from .models import Horse
from .models import Board
import random
import json

# Create your views here.

player1_first_horse = Horse.objects.get(player_name='player1', horse_number=1)

def home(request):

    return render(request, 'home.html')

def create_val(request):

    yut = Yut.objects.get(name='윷')
    #player1_first_horse = Horse.objects.get(player_name='player1', horse_number=1)
    board = Board.objects.get(name='윷놀이판')

    yut.val = random.randrange(-1,6)

    while(yut.val== 0):

        yut.val = random.randrange(-1,6)

    player1_first_horse.move_val += yut.val
    #player1_first_horse.move_val = 1 + player1_first_horse.move_val % 20

    json_str = json.dumps(board.board_coor)
    json_data = json.loads(json_str)
    coor_data = json_data[str(player1_first_horse.move_val)]

    comma = ','
    comma_pos = coor_data.find(comma)
    
    player1_first_horse.x_coor = coor_data[0:comma_pos]
    player1_first_horse.y_coor = coor_data[comma_pos+1:len(coor_data)]

    yut.save()
    player1_first_horse.save()
    board.save()

    return render(request, 'home.html', {'yut' : yut, 'player1_first_horse' : player1_first_horse})

def horse_init(request):

    player1_first_horse.move_val = 0
    player1_first_horse.x_coor=600
    player1_first_horse.y_coor=10

    return render(request, 'home.html', {'player1_first_horse' : player1_first_horse})