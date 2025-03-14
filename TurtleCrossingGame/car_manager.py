import random
from turtle import Turtle


COLORS=["red","blue","purple","green","yellow"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10

class CarManager:
    def __init__(self):
        self.all_cars=[]  # A list to store all cars
        self.car_speed=STARTING_MOVE_DISTANCE


    def create_car(self): # Code to create a new car and add it to all_cars list
        random_chance=random.randint(1,5)
        if random_chance ==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):# Code to move all cars to the left
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed  +=MOVE_INCREMENT



