#	This is for all 'aux' gauges (BOOST / COOLANT / EGT / OIL PRESSURE for now)

import pygame
from constants import *
import os 
from pygame.locals import *

global testingStatus
testingStatus = False
class AuxGauge:
	'''The AuxGauge is a class to hold and print off the aux gauge images and such'''
	def __init__(self, posxy, qty):
		self.posxy = posxy
		self.qty = qty
		self.image = 0
		self.frame = 0
		self.set_image(self.frame)
		self.grw_flag = True

	def get_image(self):
		return self.image

	def set_image(self, frame):
		'''Function to apply the int to the image, so setting the display to match the values'''
		image = str(frame)+".png"
		self.image = pygame.image.load('images/gauges/aux' + image)

	def get_pos(self):
		return (self.posxy)

	def set_frame(self, frame):
		self.frame = frame
		self.set_image(frame)

	def get_frame(self):
		return self.frame

	def show(self, screen):
		screen.blit(self.get_image(), self.get_pos())
		if testingStatus == True:
			if self.get_frame() == self.qty:
				self.grw_flag = False
			if self.get_frame() == 0:
				self.grw_flag = True
			if self.grw_flag:
				self.set_frame(self.get_frame() + 1)
			else:
				self.set_frame(self.get_frame() - 1)
		else:
			self.get_frame()