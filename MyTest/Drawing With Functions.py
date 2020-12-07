import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
snow_person1_x = 150

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()
    draw_grass()
    draw_snowman(on_draw.xxx, 140)
    draw_snowman(450, 180)
    on_draw.xxx+=1




def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snowman(x,y):
    # Draw a snow person

    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(300 + x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 340 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315 + x, 350 + y, 5, arcade.color.BLACK)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()
    on_draw.xxx=snow_person1_x
if __name__ == '__main__':
    main()
