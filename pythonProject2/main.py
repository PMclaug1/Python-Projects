import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

# detect car collision
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

# new level
    if player.ycor() > 250:
        scoreboard.add_points()
        player.reset_player()
        car_manager.increase_speed()

