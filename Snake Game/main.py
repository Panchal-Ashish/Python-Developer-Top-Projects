from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
time.sleep(2)

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:     # if snake.head.distance((food.xcor()),food.ycor()) < 15
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # detecting collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()


    # detecting collision with tail

    for segment in snake.segments[1:]:      # other than head
    # for segment in snake.segments:
        if snake.head.distance(segment) < 10:
        # if snake.head.distance(segment) < 10 and segment != snake.segments[0]:

            # if head collides with any segment in the body(tail) , we trigger the reset sequence
            scoreboard.reset()
            snake.reset()


screen.exitonclick()