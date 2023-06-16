import turtle as t
import random

tim = t.Turtle()
tim.pensize(10)
tim.speed(10)

########### Challenge 4 - Random Walk ########
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def walk():
    for _ in range(10):
        tim.forward(20)
        tim.seth(random.randrange(0,360,90))

for _ in range(10):
    tim.color(random.choice(colors))
    walk()