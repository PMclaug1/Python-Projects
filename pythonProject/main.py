import colorgram
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]


def random_color():
    new_color_dot = random.choice(color_list)
    r1 = new_color_dot[0]
    g1 = new_color_dot[1]
    b1 = new_color_dot[2]
    dot_color = (r1, g1, b1)
    return dot_color


# 10 x 10 dots - 20 circle - 50 for spaces
t.screensize(350, 350)
tim.penup()
tim.setposition(-350, -300)


def draw_circle():
    for _ in range(10):
        tim.dot(20, random_color())
        tim.penup()
        tim.forward(50)



def hirst_painting():
    for _ in range(10):
        draw_circle()
        tim.penup()
        tim.setposition(-350, (tim.ycor() + 50))

hirst_painting()

screen = t.Screen()
screen.exitonclick()