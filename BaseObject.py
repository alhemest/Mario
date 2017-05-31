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
        if not hasattr(self, 'x_size'):
            self.x_size = 40
            self.y_size = 40
        self.image_no = 0 # порядковый номер текущей картинки в массиве картинок self.images
        self.frame_no = 0 # счетчик текущего кадра
        
        # если у нас одна картинка self.image, делаем ее ресайз
        if hasattr(self, 'image'): 
            self.image = pygame.transform.scale(self.image, (self.x_size, self.y_size))
    
        # если у нас массив кртинок self.images, делаем  ресайз каждого элемента
        if hasattr(self, 'images'):
            i = 0
            for image in self.images:
                self.images[i] = pygame.transform.scale(image, (self.x_size, self.y_size))
                i += 1
    
    def choose_image(self, images, reload_delay):
        image_count = len(images) # считаем количество картинок в массиве
        
        if self.frame_no % reload_delay == 0: # когда остаток отделения равен 0
            self.image_no = (self.image_no + 1) % image_count # вычисляем номер следующей картинки
        
        self.image = images[self.image_no] # меняем картинку на следующую 
                               
    def render(self, screen):   
        screen.blit(self.image, (self.x, self.y))
        self.frame_no += 1 # после каждой отрисовки инкрементируем счетчик кадров
           
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
                    # вершины объекта
                    (self.x,                 self.y), 
                    (self.x + self.x_size,   self.y), 
                    (self.x,                 self.y + self.y_size),
                    (self.x + self.x_size,   self.y + self.y_size),
                    # точки в середине сторон объекта
                    (self.x + self.x_size/2, self.y), 
                    (self.x + self.x_size,   self.y + self.y_size/2),
                    (self.x + self.x_size/2, self.y + self.y_size),
                    (self.x,                 self.y + self.y_size/2),
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
        
