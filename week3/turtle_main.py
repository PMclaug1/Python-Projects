from turtle import Turtle, Screen
#can use from turtle import *
#will import all from module, may be confusing for some modules to know where things come from w/ multiple modules
#is not usually considered best practice. Use import "module" or from "module" import "whatever"

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("#FF5733")

for _ in range(15):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)




screen = Screen()
screen.exitonclick()