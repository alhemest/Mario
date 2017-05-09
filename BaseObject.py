'''
Created on 8 мая 2017 г.

@author: DolinnayTatiyana
'''
import pygame
from Constants import *

class BaseObject(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_size = 40
        self.y_size = 40
        self.image = pygame.transform.scale(self.image, (self.x_size, self.y_size))
    
    def render(self, screen):   
        screen.blit(self.image, (self.x, self.y))
           
    # Проверка на столкновение с объектом    
    def is_collision(self, obj):
        # Либо одна из четырех крайних точек self находится внутри obj
        for point in self.get_vertexes():
            if obj.is_inside(point):
                return True
        
        # Либо одна из четырех крайних точек obj находится внутри self
        
        for point in obj.get_vertexes():
            if self.is_inside(point):
                return True
       
        return False
    
    def get_vertexes(self):
        return [
                    (self.x,                self.y), 
                    (self.x + self.x_size,  self.y), 
                    (self.x,                self.y + self.y_size),
                    (self.x + self.x_size,  self.y + self.y_size)
                ]
        
    def is_inside(self, point):
        x = point[0]
        y = point[1]
        delta = 10
        if     (x > self.x and x < self.x + self.x_size) \
            and (y > self.y and y < self.y + self.y_size):
            # Мы выяснили, что точка (х, у) находится внутри объекта
            return True
        else:
            return False
        
