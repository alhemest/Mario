'''
Created on 9 мая 2017 г.

@author: DolinnayTatiyana
'''
import pygame
from Constants import *
from BaseObject import *

class SecretBrick(BaseObject):
    def __init__(self, x, y):
        # Загружаем изображение кирпича
        self.images = [
                        pygame.image.load("data/images/SecretBrick.png"),
                        pygame.image.load("data/images/SecretBrick1.png"),
                        pygame.image.load("data/images/SecretBrick2.png"),
                    ] 

        BaseObject.__init__(self, x, y)

        
    def render(self, screen):
        self.choose_image(self.images, reload_delay=30) # каждые 30 кадров выбирем новую картинку
        
        BaseObject.render(self, screen) # вызываем родительский рендер baseObject
       
        
    
        
