import random
import arcade
import math

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5

window = None


class Bullet(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class GamePlay(arcade.Window):


    def setup(self):

        self.all_sprites_list = arcade.SpriteList()
        self.target_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite("img/spear_man.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 70
        self.player_sprite.center_y = 70
        self.all_sprites_list.append(self.player_sprite)

        for i in range(50):

            # Create the target instance
            target = arcade.Sprite("img/target.png", SPRITE_SCALING / 30)

            # Position the target
            target.center_x = random.randrange(SCREEN_WIDTH)
            target.center_y = random.randrange(120, SCREEN_HEIGHT)

            self.all_sprites_list.append(target)
            self.target_list.append(target)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

        self.all_sprites_list.draw()

        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        bullet = Bullet("img/MB_FireRed.png", SPRITE_SCALING * 1)

        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        print("Bullet angle: {:.2f}".format(bullet.angle))


        bullet.angle = math.degrees(angle)


        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        self.all_sprites_list.append(bullet)
        self.bullet_list.append(bullet)

    def animate(self, delta_time):

        self.all_sprites_list.update()

        for bullet in self.bullet_list:

            hit_list = arcade.check_for_collision_with_list(bullet,
                                                            self.target_list)


            if len(hit_list) > 0:
                bullet.kill()

            for target in hit_list:
                target.kill()
                self.score += 1

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()


window = GamePlay(SCREEN_WIDTH, SCREEN_HEIGHT)
window.setup()

arcade.run()