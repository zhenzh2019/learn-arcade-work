""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.8
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 1
COIN_COUNT = 50
BULLET_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
zpng=["femaleAdventurer_walk0.png","femaleAdventurer_walk2.png"]


class Bullet(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)
        self.center_y = BULLET_SPEED
        pass

    def update(self):
        self.center_y += self.change_y
        if self.bottom >= SCREEN_HEIGHT:
            self.remove_from_sprite_lists()
        pass


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0
    def update(self):



        # Move the coin

        self.center_x += self.change_x

        self.center_y += self.change_y



        # If we are out-of-bounds, then 'bounce'

        if self.left < 0:

            self.change_x *= -1



        if self.right > SCREEN_WIDTH:

            self.change_x *= -1



        if self.bottom < 0:

            self.change_y *= -1



        if self.top > SCREEN_HEIGHT:

            self.change_y *= -1



class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        self.laser_sound = arcade.load_sound("laser1.ogg")
        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(zpng[1], SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("coin.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(150, SCREEN_HEIGHT)

            # coin.change_x = random.randrange(-3, 4)

            # coin.change_y = random.randrange(-3, 4)


            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        # self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        # Create a bullet
        bullet = Bullet("laserBlue01.png", SPRITE_SCALING_LASER)
        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y + 30
        bullet.change_y = BULLET_SPEED
        bullet.angle = 90
        arcade.play_sound(self.laser_sound)
        # Add the bullet to the appropriate list
        self.bullet_list.append(bullet)

    def zplayer_walk(self):
        # self.player_sprite.
        # print(self.player_sprite.filename)
        pass

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.bullet_list.update()
        self.zplayer_walk()

        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        # Generate a list of all sprites that collided with the player.
        # hit_list = arcade.check_for_collision_with_list(self.player_sprite,
        #                                                 self.coin_list)

        # if len(hit_list)>1 :
        #     print("nnnnnnnnnnnnnnnnnnnnn")
        # Loop through each colliding sprite, remove it, and add to the score.
        # for coin in hit_list:
        #     # coin.remove_from_sprite_lists()
        #     coin.center_x = random.randrange(SCREEN_WIDTH)
        #     coin.center_y = random.randrange(SCREEN_HEIGHT)
        #     self.score += 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()