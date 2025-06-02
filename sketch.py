from lib import *
import py5

center_x = py5.width // 2
center_y = py5.height // 2

def setup():
    py5.size(800, 600)
    py5.frame_rate(100)

def draw():
    py5.background(250)

    field = get_field()

    for i in range(0, field.shape[0]):
        for j in range(0, field.shape[1]):
            # Shift indices to access the field array correctly
            vec = field[i, j]
            x0 = i * 10
            y0 = j * 10
            x1 = x0 + vec[0]
            y1 = y0 + vec[1]
            draw_vector(x0, y0, x1, y1)

py5.run_sketch()
