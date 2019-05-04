from django.db import models
from jsonfield import JSONField

# Create your models here.

class Yut(models.Model):

    name = models.CharField(max_length=100, default = 'None')
    val = models.IntegerField()

    def __str__(self):

        return self.name

class Horse(models.Model):
    
    player_name = models.CharField(max_length=100, default = 'None')
    horse_number = models.IntegerField(default = 0)
    move_val = models.IntegerField()
    x_coor = models.IntegerField()
    y_coor =models.IntegerField()

    def __str__(self):

        return self.player_name + '_horse' + '('+ str(self.horse_number) +')'

class Board(models.Model):

    name = models.CharField(max_length=100, default = 'None')
    board_coor = JSONField()
    #여기부터 다시 코딩

    def __str__(self):

        return self.name