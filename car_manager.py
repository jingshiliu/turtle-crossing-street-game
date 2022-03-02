from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 2


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.level = 1

    def create_car(self):
        if random.randint(1, 30) == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setpos(400, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + (self.level - 1) * MOVE_INCREMENT)

    def next_level(self):
        self.level += 1

