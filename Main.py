'''
Created on 30 апр. 2017 г.

@author: DolinnayTatiyana
'''
import pygame
import sys
from Player import *
from Constants import *
from pygame.constants import K_RIGHT, K_LEFT, K_SPACE
from Brick import *

class Main():
    def __init__(self, screen):
        self.screen = screen 
        self.background = pygame.image.load("data/images/background.png")
        self.player = Player()
        self.objects = [Brick()]
        self.main_loop()
        
    def main_loop(self):
        while True:
            self.handle_events()
            self.render()
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN: 
                if event.key == K_RIGHT:
                    self.player.move(RIGHT)
                if event.key == K_SPACE:
                    self.player.move(UP)
                if event.key == K_LEFT:
                    self.player.move(LEFT)
            if event.type == pygame.KEYUP:
                if (event.key == K_RIGHT and self.player.position == RIGHT) \
                or (event.key == K_LEFT  and self.player.position == LEFT): 
                    self.player.stop()
                
    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.player.render(self.screen, self.objects)
        
        for obj in self.objects: 
           obj.render(self.screen) 
           
        
        if DEBUG:
            self.print_text(
                "Mario (" +
                str(self.player.x) +
                ", " +
                str(self.player.y) +
                "). " +
                "Brick: (" +
                str(self.objects[0].x) +
                ", " +
                str(self.objects[0].y + self.objects[0].y_size) +
                "). ",
                (0, 0)
            )
           
        pygame.display.flip()
        
    def print_text(self, text, point):
        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Arial', 25, True, False)
        # Render the text. "True" means anti-aliased text.
        # Black is the color. The variable BLACK was defined
        # above as a list of [0, 0, 0]
        # Note: This line creates an image of the letters,
        # but does not put it on the screen yet.
        BLACK = [0, 0, 0]
        text = font.render(text, True, BLACK)
        # Put the image of the text on the screen at 250x250
        self.screen.blit(text, point)

print ("Hello World!")
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)
