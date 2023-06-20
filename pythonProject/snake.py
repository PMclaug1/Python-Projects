import turtle
from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move_snake(self):
        # start,stop,range
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.forward(MOVE_DIST)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.forward(MOVE_DIST)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.forward(MOVE_DIST)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.forward(MOVE_DIST)
