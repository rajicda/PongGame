import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
paddle_right = Paddle(350)
paddle_left = Paddle(-350)

game_over = False
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

# Exit the program when the Escape key is pressed
screen.onkeypress(screen.bye, "Escape")
while not game_over:
    time.sleep(ball.speed)
    screen.update()
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball out of screen
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.increase_score_left()
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.increase_score_right()




screen.exitonclick()
