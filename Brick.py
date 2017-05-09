'''
Created on 7 мая 2017 г.

@author: DolinnayTatiyana
'''
import pygame
from Constants import *
from BaseObject import *

class Brick(BaseObject):
  
    def __init__(self):
        self.x = SCREEN_WIDTH / 2 + 100
        self.y = GROUND_LEVEL - 50
        self.x_size = 32
        self.y_size = 31
        
        # Загружаем изображение кирпича
        self.image = pygame.image.load("data/images/FloorBrick.png")
    
    def render(self, screen):   
        screen.blit(self.image, (self.x, self.y))

    
        