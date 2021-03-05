import pygame
from constants import *

global testingStatus
testingStatus = False

class RpmGauge:
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
		image = str(frame)+"00.png"
		self.image = pygame.image.load('images/rpm/RPM ' + image)

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