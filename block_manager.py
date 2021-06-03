from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class BlockManager:
    def __init__(self):
        self.all_rows = []
        y = 360
        for i in range(8):
            self.all_rows.append(self.create_row(y))
            y -= 60

    def create_block(self, x, y, color):
        new_block = Turtle("square")
        new_block.shapesize(stretch_len=2, stretch_wid=1)
        new_block.color()
        new_block.penup()
        new_block.color(color)
        new_block.goto(x, y)
        return new_block

    def create_row(self, y):
        x = -540
        color = random.choice(COLORS)
        row = []
        for _ in range(24):
            row.append(self.create_block(x=x, y=y, color=color))
            x += 50
        return row