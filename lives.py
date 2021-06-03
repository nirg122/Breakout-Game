import turtle as tr

class Lives(tr.Turtle):
    def __init__(self):
        super().__init__()
        self.life = 5
        self.color('pink')
        self.penup()
        self.goto(665, 310)
        self.write(f'♥\n{self.life}', align="center", font=("Courier", 25, "bold"))
        self.hideturtle()