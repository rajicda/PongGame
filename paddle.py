from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=position, y=0)

    def move_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)
