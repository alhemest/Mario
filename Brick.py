'''
Created on 7 мая 2017 г.

@author: DolinnayTatiyana
'''
import pygame
from Constants import *
from BaseObject import *

class Brick(BaseObject):
    def __init__(self, x, y):
        # Загружаем изображение кирпича
        self.image = pygame.image.load("data/images/Brick.png")
        BaseObject.__init__(self, x, y)
   

    
        