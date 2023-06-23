from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_points(self):
        self.score += 1
        self.refresh_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh_score()
