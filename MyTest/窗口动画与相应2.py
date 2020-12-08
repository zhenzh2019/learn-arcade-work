import arcade
import random
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


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
    count=0
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create a list for the balls
        self.ball_list = []

        # Add three balls to the list
        for zball in range(1,5):
            zx =random.randint(0,200)
            zy = random.randint(0, 200)
            zchange_x=random.randint(1, 50)
            zchange_y=random.randint(1, 50)
            zradius=random.randint(10, 40)
            zcolor1 = random.randint(0, 255)
            zcolor2 = random.randint(0, 255)
            zcolor3= random.randint(0, 255)
            ball = Ball(zx, zy, zchange_x, zchange_y, zradius, (zcolor1,zcolor2,zcolor3))
            self.ball_list.append(ball)

    # ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)
        # self.ball_list.append(ball)
        #
        # ball = Ball(100, 150, 2, 3, 15, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        # self.ball_list.append(ball)
        #
        # ball = Ball(150, 250, -3, -1, 15, arcade.color.FOREST_GREEN)
        # self.ball_list.append(ball)
        #

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        # Use a "for" loop to pull each ball from the list, then call the draw
        # method on that ball.
        for ball in self.ball_list:
            ball.draw()
    def on_key_press(self, symbol: int, modifiers: int):
        self.__init__(self, 640, 480, "Drawing Example")
    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""

        # Use a "for" loop to pull each ball from the list, then call the update
        # method on that ball.
        for ball in self.ball_list:
            ball.update()


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()