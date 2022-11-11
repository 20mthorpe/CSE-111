# Import the functions from the Draw 2-D library
# so that they can be used in this program.
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
    draw_sky(canvas)
    draw_ground(canvas)
    draw_cloud(canvas)
    draw_fence(canvas)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_sky(canvas):

    draw_rectangle(canvas, 0, 0, 800, 500, fill = "skyblue")

def draw_ground(canvas):

    draw_rectangle(canvas, 0, 0, 800, 100, fill = "green", outline = "green")

def draw_cloud(canvas):

    draw_oval(canvas, 100, 400, 200, 350, fill = "white", outline = "white")

def draw_fence(canvas):

    x_start = 0
    y_start = 50

    for i in range(10):
        
        draw_rectangle(canvas, x_start, y_start, 50, 200, fill = "brown", outline = "brown")
        y_start += 100
# Define your functions such as
# draw_sky and draw_ground here.



# Call the main function so that
# this program will start executing.
main()