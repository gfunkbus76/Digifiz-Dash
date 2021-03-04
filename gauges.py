from constants import *
import pygame
import os
from pygame.locals import *

class Gauge:

    #status = 0

    def __init__(self, gauge_status, gauge_pos_xy, gauge_range):
        self.gauge_status = gauge_status
        self.gauge_pos_xy = gauge_pos_xy
        self.gauge_range = gauge_range
        self.image = 0
        self.frame = 0

    def get_image(self):
        return self.image

    def get_pos(self):
        return (self.gauge_pos_xy)

    def set_image(self):
        aux_images = []
        for i in range(self.gauge_range):
            self.image = pygame.image.load("images/gauges/aux" + str(i) + ".png")
            aux_images.append(self.image)

    def draw(self, WIN):
        WIN.blit(self.get_image(), self.get_pos())
        pass
#        WIN.blit(aux_images[status], posxy)