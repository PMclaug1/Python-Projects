import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.pensize(10)
tim.speed(10)

########### Challenge 4 - Random Walk ########

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r,g,b)
    return rand_color

def walk():
    for _ in range(10):
        tim.forward(20)
        tim.seth(random.randrange(0,360,90))

for _ in range(10):
    tim.color(random_color())
    walk()