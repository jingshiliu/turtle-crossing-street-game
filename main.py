from turtle import Screen
from player import Player
from scoreboard import ScoreBoard, game_over
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
score_board = ScoreBoard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, 'w')

game_is_on = True

while game_is_on:
    time.sleep(0.001)
    screen.update()
    if player.ycor() > 300:
        player.goto(0, -300)
        score_board.next_level()
        car_manager.next_level()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            game_over()


screen.exitonclick()