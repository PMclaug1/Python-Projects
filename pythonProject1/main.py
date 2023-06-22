from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move_ball()

    # wall detection y cor

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # paddle detection

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # miss r paddle

    if ball.xcor() > 385:
        ball.reset_ball()
        scoreboard.add_points_l()

    # miss l paddle

    if ball.xcor() < - 385:
        ball.reset_ball()
        scoreboard.add_points_r()

screen.exitonclick()
