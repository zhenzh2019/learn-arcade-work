import arcade
import sys
#         find_win = win32gui.FindWindowEx(0, 0, None, title)
#         win32gui.SetWindowPos(find_win, win32con.HWND_TOPMOST, 1366,-280,800 ,600 , win32con.SWP_SHOWWINDOW)
#
#
# class MyGame(arcade.Window):
#     delta_time=6
#     def __init__(self, width, height, title):
#
#         # Call the parent class's init function
#         super().__init__(width, height, title)
#         find_win = win32gui.FindWindowEx(0, 0, None, title)
#         win32gui.SetWindowPos(find_win, win32con.HWND_TOPMOST, 1366,-280,800 ,600 , win32con.SWP_SHOWWINDOW)
#         arcade.set_background_color(arcade.color.SKY_BLUE)
#         # Attributes to store where our ball is
#         self.ball_x = 50
#         self.ball_y = 50
#
#     def on_draw(self):
#         """ Called whenever we need to draw the window. """
#
#         arcade.start_render()
#
#         arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)
#     def update(self, delta_time):
#         """ Called to update our objects. Happens approximately 60 times per second."""
#         self.ball_x += 1
#         self.ball_y += 1
#
# def main():
#     window = MyGame(640, 480, "Drawing Example")
#     # win32gui.SetWindowPos(MyGame.find_win, win32con.HWND_TOPMOST, 1367,-100,800 ,600 , win32con.SWP_SHOWWINDOW)
#     arcade.run()
#
#
import arcade

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
        # self.update()

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
    """ My window class. """

    def __init__(self, width, height, title):
        """ Constructor. """

        # Call the parent class's init function
        super().__init__(width, height, title)
        zzz = self.get_location()
        print(zzz)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.set_location(1900, -90)
        # find_win = win32gui.FindWindowEx(0, 0, None, title)
        # win32gui.SetWindowPos(find_win, win32con.HWND_TOPMOST, 1366,-280,width ,height , win32con.SWP_SHOWWINDOW)
        # Create our ball
        self.ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)
        print(type(self.ball))

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        print("--------------------------------------")

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.update()
        print("00000000000000000000000000000000")
        # yyy=self.get_location()
        # print(yyy)
        # print(delta_time)


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
