from turtle import Turtle


def game_over():
    gameOver = Turtle()
    gameOver.penup()
    gameOver.write(arg='Game Over.', font=('Courier', 30, 'normal'), align='center')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-380, 250)
        self.level = 1
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', align='left', font=('Courier', 30, 'normal'))

    def next_level(self):
        self.level += 1
        self.update_level()
