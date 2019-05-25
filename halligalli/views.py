from django.shortcuts import render,redirect
import time
import random
import json
import time
import datetime

from .models import Player
from .models import Card

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.

com1 = Player.objects.get(player_name = 'Computer1')
com2 = Player.objects.get(player_name = 'Computer2')
com3 = Player.objects.get(player_name = 'Computer3')
user = Player.objects.get(player_name = 'User')
card = Card.objects.get(owner = 'None')

global com1_cnt
global com2_cnt
global com3_cnt
global user_cnt
global end_check
global time_diff_sum


def home(request):

    init_player()
    players = Player.objects.order_by('-player_score')
    return render(request,'home.html', {'players':players})

def play_game(request):

    init_player()

    global com1_cnt
    global com2_cnt
    global com3_cnt
    global user_cnt
    global time_diff_list
    global time_diff_sum
    time_diff_list = []

    com1_cnt = 0
    com2_cnt = 0
    com3_cnt = 0
    user_cnt = 0

    return render(request, 'play_game.html', {'com1' : com1,'com2' : com2,'com3' : com3, 'user' : user, 'com1_cnt' : com1_cnt, 'com2_cnt' : com2_cnt,'com3_cnt' : com3_cnt,'user_cnt' :user_cnt})

def show_card(request):

    global com1_num
    global com2_num
    global com3_num
    global user_num
    global time_average

    json_str = json.dumps(card.card_info)
    json_data = json.loads(json_str)
    
    if(com1.card_num!=0):
        com1_num = random.randrange(1,21)
        com1.current_card = json_data[str(com1_num)]
    
    if(com2.card_num!=0):
        com2_num = random.randrange(1,21)
        com2.current_card = json_data[str(com2_num)]

    if(com3.card_num!=0):
        com3_num = random.randrange(1,21)
        com3.current_card = json_data[str(com3_num)]

    if(user.card_num !=0):
        
        user_num = random.randrange(1,21)
        user.current_card = json_data[str(user_num)]

    global my_time1
    my_time1 = time.time()

    global com1_cnt
    global com2_cnt
    global com3_cnt
    global user_cnt

    if(com1.card_num > 0):
        com1.card_num = com1.card_num-1
        com1_cnt = com1_cnt+1

    if(com2.card_num > 0):
        com2.card_num = com2.card_num-1
        com2_cnt = com2_cnt+1

    if(com3.card_num > 0):
        com3.card_num = com3.card_num-1
        com3_cnt = com3_cnt+1

    if(user.card_num > 0):
        user.card_num = user.card_num-1
        user_cnt = user_cnt+1

    end_check = 0
    
    if(user.card_num == 60):
        print('end_check 값 바꾸기')
        end_check = 1

    time.sleep(1)

    return render(request, 'play_game.html', {'com1' : com1,'com2' : com2,'com3' : com3, 'user' : user,  'com1_cnt' : com1_cnt, 'com2_cnt' : com2_cnt,'com3_cnt' : com3_cnt,'user_cnt' : user_cnt,'end_check' : end_check})

def confirm(request):


    fruit_list = {'banana' :0, 'lime' :0, 'strawberry' :0, 'plum' : 0}

    end_check = 0
    com1_comma = com1.current_card.find(',')
    com2_comma = com2.current_card.find(',')
    com3_comma = com3.current_card.find(',')
    user_comma = user.current_card.find(',')

    com1_fruit = com1.current_card[0:com1_comma]
    com1_num = com1.current_card[com1_comma+2:com1_comma+3]

    com2_fruit = com2.current_card[0:com2_comma]
    com2_num = com2.current_card[com2_comma+2:com2_comma+3]

    com3_fruit = com3.current_card[0:com3_comma]
    com3_num = com3.current_card[com3_comma+2:com3_comma+3]
    
    user_fruit = user.current_card[0:user_comma]
    user_num = user.current_card[user_comma+2:user_comma+3]

    if(user.current_card !='None'):    
        user_list = {user_fruit : int(user_num)}
        c1 = {com1_fruit : int(com1_num)}
        c2 = {com2_fruit : int(com2_num)}
        c3 = {com3_fruit : int(com3_num)}

        for key,val in fruit_list.items():
            if key in user_list:
                fruit_list[key] = fruit_list[key] + user_list[key]

        for key,val in fruit_list.items():
            if key in c1:
                fruit_list[key] = fruit_list[key] + c1[key]

        for key,val in fruit_list.items():
            if key in c2:
                fruit_list[key] = fruit_list[key] + c2[key]

        for key,val in fruit_list.items():
            if key in c3:
                fruit_list[key] = fruit_list[key] + c3[key]

    my_time2 = time.time()

    print('여기')
    print(fruit_list)

    try :
        time_diff = round(float(my_time2),3) - round(float(my_time1),3)
        time_diff = round(time_diff,3)
   
    except NameError :
        time_diff = 'none'

    time_diff_pre = float(my_time2) - float(my_time1)
    time_diff = round(time_diff_pre,5)
    
    global com1_cnt
    global com2_cnt
    global com3_cnt
    global user_cnt
    signal =False

    for key,val in fruit_list.items():
        if(fruit_list[key] ==5):
            signal = True
            print(signal)

    if(com1.current_card == 'None'):
        confirm_message = '카드가 아직 공개되지 않았습니다!\n카드 공개를 클릭해서 게임을 시작해보세요!'

    elif(signal):
        time_diff_list.append(time_diff)
        confirm_message = '정답!\nuser가 ' +str(com1_cnt + com2_cnt + com3_cnt + user_cnt) +'개의 카드들을 획득했습니다!'
        user.card_num = user.card_num + com1_cnt +  com2_cnt + com3_cnt + user_cnt
        com1_cnt =0
        com2_cnt =0
        com3_cnt =0
        user_cnt=0

    else:
        confirm_message = '오답!\n과일의 개수가 5개가 아닙니다\ncomputer에게 카드를 1개씩 나눠줍니다!'
        com1.card_num = com1.card_num + 1
        com2.card_num = com2.card_num + 1
        com3.card_num = com3.card_num + 1
        user.card_num = user.card_num -3

    if(user.card_num <=0):
        end_check =2

    time_diff_sum = 0
    if len(time_diff_list) > 0:
        for i in range(0,len(time_diff_list),1):
            time_diff_sum = time_diff_sum+time_diff_list[i]
        time_average_pre = time_diff_sum/len(time_diff_list)
        time_average = round(time_average_pre,5)  

    else:
        time_average = '평균시간은 정답일때만 나와요.'


    return render(request, 'play_game.html',{'com1' : com1,'com2' : com2,'com3' : com3,  'user' : user, 'confirm_message' : confirm_message, 'time_diff' : 
    time_diff,  'com1_cnt' : com1_cnt, 'com2_cnt' : com2_cnt,'com3_cnt' : com3_cnt,'user_cnt' : user_cnt, 'end_check' : end_check, 'time_average' : time_average})

def init_player():

    com1.player_name = 'Computer1'
    com1.comment = 'None'
    com1.card_num = 15
    com1.score = 0
    com1.current_card='None'
    com1.bell_flag=0

    
    com2.player_name = 'Computer2'
    com2.comment = 'None'
    com2.card_num = 15
    com2.score = 0
    com2.current_card='None'
    com2.bell_flag=0

    
    com3.player_name = 'Computer3'
    com3.comment = 'None'
    com3.card_num = 15
    com3.score = 0
    com3.current_card='None'
    com3.bell_flag=0

    user.player_name = 'User'
    user.userment = 'None'
    user.card_num = 15
    user.score = 0
    user.current_card='None'
    user.bell_flag=0

def end_check(request):

    return render(request, 'end_check.html')

def register(request):

    if request.method == 'POST':
        player = Player()
        player.player_name = request.POST['name']
        player.player_comment = request.POST['comment']
        player.save()
        
    return render(request, 'home.html')

def end_check2(request):
    
    return render(request, 'end_check2.html')