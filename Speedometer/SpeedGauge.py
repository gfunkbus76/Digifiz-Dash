import pygame
import os 
from pygame.locals import *
# THIS IS FOR A Speed GAUGE

#Speed Gauge Class
class SpeedGauge:
	def __init__(self, posx, posy, textx, texty):
		self.posx = posx
		self.posy = posy
		self.image = 0
		self.frame = 'speed'
		self.set_image(self.frame)
		#self.grw_flag = True
		self.speed = "0"
		#RPi Font
		#self.font = pygame.font.Font('/home/pi/Gauge/Speedometer/digital-7.ttf', 60)
                #Windows Font
		self.font = pygame.font.SysFont('DIGITAL-7.ttf', 60)
		self.text = 0
		self.textx = textx
		self.texty = texty

	def get_image(self):
		return self.image

	def set_image(self, frame):
		image = str(frame)+".png"
		self.image = pygame.image.load('Speedometer/' + image)

	def get_pos(self):
		return (self.posx, self.posy)

	def get_textpos(self):
		return (self.textx, self.texty)

	def set_frame(self, frame):
		self.frame = frame
		self.set_image(frame)

	def get_frame(self):
		return self.frame

	def set_speed(self, speed):
		self.speed = str(speed)

	def get_speed(self):
		return int(self.speed)

	def show(self, screen):
		screen.blit(self.get_image(), self.get_pos())

		self.text = self.font.render(self.speed, True, (0, 0, 0))
		self.textx -= self.text.get_rect().right
		screen.blit(self.text, self.get_textpos())
		self.textx += self.text.get_rect().right
		self.refresh()

	def refresh(self):
		self.set_speed(self.get_speed() + 1)
