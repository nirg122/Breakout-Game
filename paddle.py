import turtle as tr

class Paddle:
    def __init__(self):
        self.paddle_list = []
        x = 0
        for _ in range(6):
            self.paddle_list.append(self.create_paddle_pixel(x))
            x += 20

    def create_paddle_pixel(self, x):
        pixel = tr.Turtle()
        pixel.shape("square")
        pixel.shapesize(stretch_len=1, stretch_wid=0.5)
        pixel.color("black")
        pixel.penup()
        pixel.setpos((x, -350))
        return pixel
