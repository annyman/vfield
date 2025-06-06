from vector import *
import py5

last_time = None

def setup():
    py5.size(res.x, res.y)
    py5.frame_rate(60)
    global last_time
    last_time = py5.millis()

def draw():
    py5.background(250)

    field = get_field()

    global last_time
    now = py5.millis()
    delta_time = (now - last_time) / 1000.0  # delta_time in seconds
    last_time = now

    for i in range(0, field.shape[0]):
        for j in range(0, field.shape[1]):
            vec = field[i, j]
            x0 = i * scale
            y0 = j * scale
            x1 = x0 + vec[0]
            y1 = y0 + vec[1]
            draw_vector(x0, y0, x1, y1)

py5.run_sketch()
