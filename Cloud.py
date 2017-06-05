'''
Created on 31 мая 2017 г.

@author: DolinnayTatiyana
'''

import pygame
from Constants import *
from BaseObject import *

class Cloud(BaseObject):
    def __init__(self, x, y, is_big):
        # Загружаем изображение облака
        if is_big:
            self.x_size = 60*2
            self.y_size = 55
            self.image = pygame.image.load("data/images/BigCloud.png")
        else:
            self.x_size = 60
            self.y_size = 55
            self.image = pygame.image.load("data/images/Cloud.png")
                    
        BaseObject.__init__(self, x, y)
        
        self.is_background = True