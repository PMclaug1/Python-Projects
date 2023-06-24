from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

with open("high_score.txt") as high_score:
    contents = high_score.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(contents)
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
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.refresh_score()
