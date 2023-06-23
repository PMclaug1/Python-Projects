from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0, 270)
        self.refresh_score()

    def refresh_score(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align=ALIGNMENT, font=FONT)

    def add_points(self):
        self.score += 1
        self.clear()
        self.refresh_score()
