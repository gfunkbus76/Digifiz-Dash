import pygame
from menu import *


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.DISPLAY_W, self.DISPLAY_H = 1920, 720
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.background = pygame.image.load("images/background.png")
        self.font_name = 'fonts/DSEG7Classic-Bold.ttf'
        self.maintextHighlight, self.maintextInactiveBG, self.maintextLowHighlight = (236, 253, 147), (9, 52, 50), (145, 213, 89)
        self.font_size, self.font_size_lower = (174), (94)

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.blit(self.background, (0, 0))
            self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)


