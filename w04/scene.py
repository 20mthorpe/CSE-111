# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from tkinter import Y
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 2,
        scene_width, scene_height, width=0, fill="deepSkyBlue")
    
    draw_clouds(canvas)

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 2, width=0, fill="Green")
    draw_grass(canvas)
    
    # Draw a pine tree.
    tree_center_x = 190
    tree_bottom = 100
    tree_height = 300
    draw_pine_tree(canvas, tree_center_x,
    tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 250
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="darkGreen")


def draw_clouds(canvas):
    for i in range(40):
        scene_width = 800
        scene_height = 500
        half_height = round(scene_height)
        min_diam = 30
        max_diam = 80
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter + 50, y + diameter,
            fill="aliceBlue", outline = "aliceBlue")

def draw_grass(canvas):
    for i in range(200):
        location_x = random.randint(0, 800)
        location_y = random.randint(0, 250)

        draw_line(canvas, location_x,location_y,location_x,location_y+20, fill="darkGreen", width=3)


# Call the main function so that
# this program will start executing.
main()