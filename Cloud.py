'''
Created on 31 мая 2017 г.

@author: DolinnayTatiyana
'''

import pygame
from Constants import *
from BaseObject import *

class Cloud(BaseObject):
    def __init__(self, x, y):
        # Загружаем изображение облака
        self.x_size = 60
        self.y_size = 55
        
        self.image = pygame.image.load("data/images/Cloud.png")
        
        BaseObject.__init__(self, x, y)