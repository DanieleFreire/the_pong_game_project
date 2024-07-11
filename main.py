from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((410, 0))
l_paddle = Paddle((-410, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

#moves ball
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380:
        ball.bounce_x()


    #Detect when r_paddle misses
    if ball.xcor() > 440:
        ball.reset_position()
        scoreboard.l_point()

    #Detect when l_paddle misses
    if ball.xcor() < -440:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

