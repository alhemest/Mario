'''
Created on 7 мая 2017 г.

@author: DolinnayTatiyana
'''
import pygame
from Constants import *
from BaseObject import *

class Brick(BaseObject):
  
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_size = 40
        self.y_size = 40
        
        # Загружаем изображение кирпича
        self.image = pygame.image.load("data/images/Brick.png")
        self.image = pygame.transform.scale(self.image, (self.x_size, self.y_size))
   

    
        