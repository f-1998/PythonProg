from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenia")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()

    if scoreboard.score <= 5:
        time.sleep(0.5)
    elif 5 < scoreboard.score < 10:
        time.sleep(0.3)
    else:
        time.sleep(0.1)
    snake.turn()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for s in snake.segs[1:]:
        if snake.head.distance(s) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
