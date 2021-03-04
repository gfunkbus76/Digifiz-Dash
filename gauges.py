from constants import *
import pygame
import os
from pygame.locals import *

class Gauge:

    #status = 0

    def __init__(self, status, posxy, range):
        self.status = status
        self.posxy = posxy
        self.range = range
        self.image = 0
        self.frame = 0

    def get_image(self):
        return self.image

    def get_pos(self):
        return (self.posxy)

    def set_image(self):
        aux_images = []
        for i in range([range]):
            self.image = pygame.image.load("images/gauges/aux" + str(i) + ".png")
            aux_images.append(self.image)

    def draw(self, WIN):
        WIN.blit(self.get_image(), self.get_pos())
        pass
#        WIN.blit(aux_images[status], posxy)