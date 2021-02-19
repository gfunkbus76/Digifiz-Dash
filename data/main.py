"""
The main function is defined here. It creates an instance of
Control starts up the main program.
"""

import pygame

pygame.init()


class Digi:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 60
        self.background = (0, 0, 0)

    def start(self):
        pass

    def logic(self):
        pass

    def render(self, window):
        self.win.fill(self.background)

        pygame.display.update()
