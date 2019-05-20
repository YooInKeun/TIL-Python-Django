from django.db import models
from jsonfield import JSONField

# Create your models here.

class Player(models.Model):
    
    player_name = models.CharField(max_length=100, default = 'None')
    comment = models.TextField(max_length = 20, default = 0)
    card_num = models.IntegerField()
    score = models.IntegerField()
    current_card = models.CharField(max_length=100, default = 'None')
    bell_flag =models.IntegerField()

    def __str__(self):

        return self.player_name

class Card(models.Model):

    owner = models.CharField(max_length=100, default = 'None')
    card_info = JSONField()

    def __str__(self):

        return self.owner + ' 카드'
