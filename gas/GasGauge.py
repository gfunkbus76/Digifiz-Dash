import pygame
import os 
from pygame.locals import *
# THIS IS FOR A GAS GAUGE

#Gas Gauge Class
class GasGauge:
	def __init__(self, posx, posy):
		self.posx = posx
		self.posy = posy
		self.image = 0
		self.frame = 0
		self.set_image(self.frame)
		self.grw_flag = True

	def get_image(self):
		return self.image

	def set_image(self, frame):
		image = str(frame)+".png"
		self.image = pygame.image.load('gas/' + image)

	def get_pos(self):
		return (self.posx, self.posy)

	def set_frame(self, frame):
		self.frame = frame
		self.set_image(frame)

	def get_frame(self):
		return self.frame

	def show(self, screen):
		screen.blit(self.get_image(), self.get_pos())
		if self.get_frame() == 15:
			self.grw_flag = False
		if self.get_frame() == 0:
			self.grw_flag = True
		if self.grw_flag:
			self.set_frame(self.get_frame() + 1)
		else:
			self.set_frame(self.get_frame() - 1)