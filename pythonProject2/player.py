from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        if self.ycor() < 250:
            self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)

