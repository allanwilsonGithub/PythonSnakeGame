from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 28, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-10, 450)
        self.hideturtle()
        self.score = 0
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()
