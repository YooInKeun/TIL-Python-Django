import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yutproject.settings")
import django
django.setup()
from yut.models import Yut
from yut.models import Horse
from yut.models import Board

if __name__=='__main__':

    Yut(name = '윷', val = 0).save()
    Horse(player_name = 'player1', horse_number = 1, move_val = 0, x_coor = 600, y_coor = 10).save()
    Board(name= '윷놀이판', board_coor ={1: '400,320', 2: '400,240', 3:'400,160', 4:'400,80', 5: '400,0',
    6: '320,0', 7: '240,0', 8:'160,0', 9:'80,0', 10:'0,0', 11:'0,80', 12:'0,160', 13:'0,240', 14:'0,320',
    15:'0,400', 16: '80,400', 17: '160,400', 18:'240,400', 19: '320,400', 20:'400,400'}).save()