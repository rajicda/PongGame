from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0.1
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_ball_speed()

    def reset(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.bounce_x()

    def increase_ball_speed(self):
        if self.speed > 0.00001:
            self.speed *= 0.9

