'''
Created on 30 апр. 2017 г.

@author: DolinnayTatiyana
'''
import pygame
from Constants import *
from BaseObject import *

class Player(BaseObject):
    def __init__(self):
        self.position = RIGHT
        self.on_the_ground = True
        self.x = SCREEN_WIDTH / 2
        self.y = GROUND_LEVEL
        self.Vx = 0
        self.Vy = 0
        self.x_size = 45
        self.y_size = 60  
        
        # Загружаем изображения игрока
        self.images = []
        images_pack = ["MarioLeft.png", "MarioRight.png"]
        for image in images_pack: 
            self.images.append( pygame.image.load("data/images/" + image) )
            
    def move(self, direction):
        if direction == RIGHT:
            self.position = RIGHT
            self.Vx = 1
        if direction == LEFT:
            self.position = LEFT
            self.Vx = -1
        if direction == UP:
            if self.on_the_ground == True:
                self.Vy = -JUMP_SPEED
                self.on_the_ground = False
            
    def stop(self):
        self.Vx = 0
        
        # Отрисовка игрока
    def render(self, screen, objects):
        # Вычисление новых координат в зависимости от текущей скорости
        self.x += self.Vx
        self.y += self.Vy
              
        # когда игрок прилетает сверху на землю, останавливаем его
        if self.y >= GROUND_LEVEL:
            self.on_the_ground = True
            self.Vy = 0
        
        # взаимодействие игрока с кирпичем по его боковым точкам
        for obj in objects: 
            # Если произошло столкновение
            if self.is_collision(obj):
                # Телепортируем игрока к ближайшей границе
                # Обнуляем горизонтальную либо вертикальную скорость
                # Если мы прилетели сверху, то устанавливаем флаг on_the_ground
                delta_x_left = obj.x - (self.x + self.x_size) # лев стены, прав игрока 
                delta_x_right = (obj.x + obj.x_size) - self.x # прав стены, лев игрока
                if (abs(delta_x_left) < abs(delta_x_right)):
                    delta_x = delta_x_left
                else:
                    delta_x = delta_x_right
             
                delta_y_up = obj.y - (self.y + self.y_size)  # верх стены, низ игрока
                delta_y_down = (obj.y + obj.y_size) - self.y # них стены, верх игрока
                if (abs(delta_y_up) < abs(delta_y_down)):
                    delta_y = delta_y_up
                else:
                    delta_y = delta_y_down
            
                if (abs(delta_x) < abs(delta_y)):
                    self.x += delta_x
                    self.Vx = 0
                else:
                    self.y += delta_y
                    self.Vy = 0
                    if delta_y < 0:
                        self.on_the_ground = True

        # действие гравитации, если игрок не на земле
        if not self.on_the_ground:
            self.Vy += G  
        
                
        # размещаем картинку игрока по текущим координатам игрока    
        screen.blit(self.images[self.position], (self.x, self.y))
 