from turtle import Turtle

PLAYER_SPEED = 10


class Player(Turtle):
    """Says Car but actually a turtle that cross street"""

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def up(self):
        self.goto(0, self.ycor() + PLAYER_SPEED)
