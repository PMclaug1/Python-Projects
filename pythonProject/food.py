from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.res_food()

    def res_food(self):
        rand_x = random.randint(-275, 275)
        rand_y = random.randint(-275, 225)
        self.goto(rand_x, rand_y)
