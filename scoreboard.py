from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto((40, 170))
        self.write(f"{self.score_right}", align=ALIGNMENT, font=FONT)
        self.goto((-40, 170))
        self.write(f"{self.score_left}", align=ALIGNMENT, font=FONT)

    def increase_score_right(self):
        self.score_right += 1
        self.update_score()

    def increase_score_left(self):
        self.score_left += 1
        self.update_score()