'''
Created on 30 апр. 2017 г.

@author: DolinnayTatiyana
'''
import pygame
from Constants import *
from BaseObject import *
from gc import get_objects
from time import sleep

class Player(BaseObject):
    def __init__(self, x, y):
        BaseObject.__init__(self, x, y)
        self.position = RIGHT
        self.on_the_ground = True
        self.Vx = 0
        self.Vy = 0
        self.is_moving = 0
        self.sound = {
            "jump": pygame.mixer.Sound("data/sounds/smb_jump-small.wav"), 
            "bump": pygame.mixer.Sound("data/sounds/smb_bump.wav")
            }
         
        # Загружаем изображения игрока
        self.images = {
            'small':        pygame.image.load("data/images/MarioRight.png"),
            'small_jump':   pygame.image.load("data/images/MarioJump.png"),
            'small_run':    [  
                               #pygame.image.load("data/images/MarioRun.png"),
                               pygame.image.load("data/images/MarioRun2.png"),
                               pygame.image.load("data/images/MarioRun1.png"),
                               
                            ],
            }
        
        
        for key in self.images:
            if isinstance(self.images[key], list):
                # Если у нас массив картинок
                for i in range(0, len(self.images[key])):
                    w = self.images[key][i].get_width()
                    h = self.images[key][i].get_height()
                    y = self.y_size
                    x = int(w * self.y_size / h)
                    # ресайз всех загруженных в список изображений
                    self.images[key][i] = pygame.transform.scale(self.images[key][i], (x, y))
            else:
                # Если у нас одиночная картинка
                w = self.images[key].get_width()
                h = self.images[key].get_height()
                y = self.y_size
                x = int(w * self.y_size / h)
                # ресайз всех загруженных в список изображений
                self.images[key] = pygame.transform.scale(self.images[key], (x, y))
        
        
           
            
    def move(self, direction):
        if direction == RIGHT:
            self.position = RIGHT
            self.is_moving = 2
        if direction == LEFT:
            self.position = LEFT
            self.is_moving = -2
        if direction == UP:
            if self.on_the_ground == True:
                self.Vy = -JUMP_SPEED
                self.on_the_ground = False
                self.sound["jump"].play()
                
            
    def stop(self):
        self.is_moving = 0
        
        # Отрисовка игрока
    def render(self, screen, objects):
        # Придаем горизонтальную скорость, если игрок в состоянии движения
        self.Vx = self.is_moving
        
        # Вычисление новых координат в зависимости от текущей скорости
        self.x += self.Vx
        self.y += self.Vy
              
        
        # когда игрок прилетает сверху на землю, останавливаем его
        if self.y >= GROUND_LEVEL:
            self.on_the_ground = True
            self.y = GROUND_LEVEL
            self.Vy = 0
        else:
            if self.on_the_ground:
                self.in_air_detect(objects)

        
        self.calculate_collisions(objects)
        
        # действие гравитации, если игрок не на земле
        if not self.on_the_ground:
            self.Vy += G  
        
                
        # размещаем картинку игрока по текущим координатам игрока 
        if self.on_the_ground:
            self.image = self.images['small']
            if self.is_moving != 0:
                self.choose_image(self.images['small_run'], reload_delay=7) 
        else:
            self.image = self.images['small_jump']           
        
        
        
        # При необходимости отражаем картинку по вертикали (чтобы смотрела влево)
        if self.position == LEFT:
            self.image = pygame.transform.flip(self.image, True, False)
                
        BaseObject.render(self, screen)

    def in_air_detect(self, objects):
        for i in range(int(self.x), int(self.x + self.x_size)):
            point = (i, self.y + self.y_size + 1)
            for obj in objects:
                if obj.is_inside(point):
                    self.on_the_ground = True
                    return
        print("IN AIR!")
        self.on_the_ground = False
 
    def calculate_collisions(self, objects):
        # взаимодействие игрока с кирпичем по его боковым точкам
        for obj in objects: 
            # Если произошло столкновение
            if self.is_collision(obj):
                # Телепортируем игрока к ближайшей границе
                # Обнуляем горизонтальную либо вертикальную скорость
                # Если мы прилетели сверху, то устанавливаем флаг on_the_ground
                delta_x_left = obj.x - (self.x + self.x_size) # лев стены, прав игрока 
                delta_x_right = (obj.x + obj.x_size) - self.x # прав стены, лев игрока
                if (abs(delta_x_left) < abs(delta_x_right)):  # вычисление более близкого расстояния для телепортации влево или вправо
                    delta_x = delta_x_left
                else:
                    delta_x = delta_x_right
             
                delta_y_up = obj.y - (self.y + self.y_size)  # верх стены, низ игрока
                delta_y_down = (obj.y + obj.y_size) - self.y # них стены, верх игрока
                if (abs(delta_y_up) < abs(delta_y_down)):    # вычисление более близкого расстояния для телепортации вверх или вниз
                    delta_y = delta_y_up
                else:
                    delta_y = delta_y_down
            
                if (abs(delta_x) < abs(delta_y)):  # вычисление более близкого расстояния для телепортации по горизонтали или вертикали
                    self.x += delta_x
                    self.Vx = 0
                else:
                    self.y += delta_y
                    self.Vy = 0
                    if delta_y < 0:
                        print("ground")
                        self.on_the_ground = True
                    else:
                        print("sound") 
                        self.sound["bump"].play()
