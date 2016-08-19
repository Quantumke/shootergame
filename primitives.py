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

class TheGame(arcade.Window):
	def setup(self):
		#setup the sprites :)
		self.all_sprites_list=arcade.SpriteList()
		self.target_list=arcade.SpriteList()
		self.bullet_list=arcade.SpriteList()

		#set up thr player:)
		self.score=0
		self.player_sprite = arcade.Sprite("img/Shooting.gif", SPRITE_SCALING)
		self.player_sprite.center_x= 50
		self.player_sprite.center_y= 70
		self.all_sprites_list.append(self.player_sprite)

		for i in range(50):
			#create taget instance
			target=arcade.Sprite("img/target.png", SPRITE_SCALING / 3)
			#target positions :)
			target.center_x= random.randrange(SCREEN_HEIGHT)
			target.center_y= random.randrange(120, SCREEN_HEIGHT)

			self.all_sprites_list.append(target)
			self.target_list.append(taget)

			arcade.set_backgroung_color(arcade.AMAZON)
	def on_draw(self):
		arcade.start_render()
		self.all_sprites_list.draw()
		score= "Score:{}".format(self.score)
		arcade.draw_text(score, 10, 20 , arcade.color.WHITE, 14)
	def on_mouse_press(self, x, y, button, modifiers):
		arcade.set_backgroung_color(arcade.WHITE 6)
		bullet= RamboBullets("img/taget.png", SPRITE_SCALING * 1.5)
		start_x=self.player_sprite.center_x
		start_y=self.player_sprite.center_y
		bullet.center_x=start_x
		bullet.center_y=start_y

		#aim from mouse
		dest_x=x
		dest_y=y

		#get angle of bullet
		x_diff= dest_x - start_x
		y_diff= dest_y - start_y
		angle= math.atan2(y_diff, x_diff)
		print ("Bullet angle:{: .2f}". format(bullet.angle))
		bullet.angle = math.degrees(angle)
		bullet.change_x = math.cos(angle) * BULLET_SPEED
		bullet.change_y= math.sin(angle) * BULLET_SPEED

		self.all_sprites_list.append(Bullet)
		self.bullet_list.append(bullet)
		




