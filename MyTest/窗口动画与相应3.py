import arcade
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3

class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):
    count = 0

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        # self.set_location(1900, -90)
        arcade.set_background_color(arcade.color.ASH_GREY)
        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        # self.set_mouse_visible(False)

        # Create a list for the balls
        self.ball_list = []
        self.ball_ref()
        self.xball = Ball(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,0,0,20,arcade.color.AUBURN)


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.xball.draw()
        # Use a "for" loop to pull each ball from the list, then call the draw
        # method on that ball.
        for ball in self.ball_list:
            ball.draw()

    def ball_ref(self):
        # self.ball_list = []
        # Add three balls to the list
        for zzball in range(0, 4):
            zx = random.randint(0, 200)
            zy = random.randint(0, 200)
            zchange_x = random.randint(1, 10)
            zchange_y = random.randint(1, 10)
            zradius = random.randint(10, 40)
            zcolor1 = random.randint(0, 255)
            zcolor2 = random.randint(0, 255)
            zcolor3 = random.randint(0, 255)
            ball = Ball(zx, zy, zchange_x, zchange_y, zradius, (zcolor1, zcolor2, zcolor3))
            if len(self.ball_list) < 4:
                self.ball_list.append(ball)
            else:
                self.ball_list[zzball] = ball
            self.xball = Ball(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,0,0,20,arcade.color.AUBURN)

    def speed_change(self, zway):
        xx = 0
        yy = 0
        mxx = 0
        myy = 0
        if zway == "u":
            yy = 1
        elif zway == "d":
            yy = -1
        elif zway == "l":
            xx = -1
        elif zway == "r":
            yy = 1
        elif zway == "a":
            mxx = -1
        elif zway == "w":
            myy = 1
        elif zway == "dd":
            mxx = 1
        elif zway == "s":
            myy = -1

        for zc in range(0, 4):
            if self.ball_list[zc].change_x != 0:
                self.ball_list[zc].change_x = xx * self.ball_list[zc].change_x / abs(self.ball_list[zc].change_x) + \
                                              self.ball_list[zc].change_x
            else:
                self.ball_list[zc].change_x = xx + self.ball_list[zc].change_x

            if self.ball_list[zc].change_y != 0:
                self.ball_list[zc].change_y = yy * self.ball_list[zc].change_y / abs(self.ball_list[zc].change_y) + \
                                              self.ball_list[zc].change_y
            else:
                self.ball_list[zc].change_y = yy + self.ball_list[zc].change_y
            print(self.ball_list[zc].change_x, self.ball_list[zc].change_y)
        print(mxx,myy)
        self.xball.change_x= mxx * MOVEMENT_SPEED
        self.xball.change_y= myy * MOVEMENT_SPEED


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            print("Left key hit")
            self.speed_change("l")
        if key == arcade.key.UP:
            self.speed_change("u")
            print("Up key hit")
        if key == arcade.key.RIGHT:
            print("Right key hit")
            self.speed_change("r")
        if key == arcade.key.DOWN:
            self.speed_change("d")
            print("Down key hit")
        if key == arcade.key.A:
            print("A key hit")
            self.speed_change("a")
        if key == arcade.key.W:
            self.speed_change("w")
            print("W key hit")
        if key == arcade.key.D:
            print("D key hit")
            self.speed_change("dd")
        if key == arcade.key.S:
            self.speed_change("s")
            print("S key hit")
        elif key == arcade.key.SPACE:
            print("The 'Space' key was hit")
            self.ball_ref()

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.xball.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.xball.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""

        # # Use a "for" loop to pull each ball from the list, then call the update
        # method on that ball.

        for ball in self.ball_list:
            ball.update()
        self.xball.update()


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
