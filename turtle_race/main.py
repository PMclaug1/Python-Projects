from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
player_choice = screen.textinput(title="bet", prompt="Who will win the race? Pick a color: ")
print(player_choice)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-80, -48, -16, 16, 48, 80]
turtle_racers = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=-y_pos[turtle])
    turtle_racers.append(new_turtle)

if player_choice:
    is_race_on = True

while is_race_on:
    for turtle in turtle_racers:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == player_choice:
                print(f"You've won! The {winner} turtle is the winner.")
            else:
                print(f"You've lost! The {winner} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

#turtle is 40x40
