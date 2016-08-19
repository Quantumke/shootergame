import arcade
import math 
import random

#set up sprite:
SPRITE_SCALING=0.5
SCREEN_WIDTH=600
SCREEN_HEIGHT=600
BULLET_SPEED=5
window=none

class RamboBullets(arcade.Sprite):
	def update(self):
		self.center_x+=self.change_x
		self.center_y+=self.change_y
