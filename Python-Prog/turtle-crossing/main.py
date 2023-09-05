import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car.create_cars()
    car.move_car()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 290:
        score.level_up()
        player.goto(0, -280)
        car.speed()







screen.exitonclick()