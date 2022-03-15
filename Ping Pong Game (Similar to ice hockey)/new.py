from turtle import *
from paddle import *
from ball import Ball
from scoreboard import *
import random
import time

screen = Screen()
screen.screensize(canvwidth=800,canvheight=600, bg="black")
screen.title("Ping Pong game")
screen.tracer(0)

r_paddle = Paddle((370,0))
l_paddle = Paddle((-370,0))
ball = Ball()
scoreboard = Scoreboard()
time.sleep(2)

screen.listen()
screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

screen.onkey(key="w",fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    # detecting ball collision with wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()

    # detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 345 or ball.distance(l_paddle) < 50 and ball.xcor() < -345:
        ball.bounce_x()
        time.sleep(ball.move_speed)

    # detect when right paddle misses
    if ball.xcor() > 375:
        ball.reset()
        scoreboard.l_point()


    # detect when left paddle misses
    if ball.xcor() < -375:
        ball.reset()
        scoreboard.r_point()

    # winner
    if scoreboard.r_score >= 5:
        scoreboard.winner("right side player")
        game_on = False

    if scoreboard.l_score >= 5:
        scoreboard.winner("left side player")
        game_on = False


screen.exitonclick()