from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.refresh_score()

    def refresh_score(self):
        self.write(f"Scoreboard: {self.l_score} - {self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align=ALIGNMENT, font=FONT)

    def add_points_l(self):
        self.l_score += 1
        self.clear()
        self.refresh_score()

    def add_points_r(self):
        self.r_score += 1
        self.clear()
        self.refresh_score()
