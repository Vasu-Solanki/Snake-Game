from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """In this we give color and size to the food.
        This Food class inheritance of Turtle class."""
        super().__init__()
        # Calling self.shape = Tutle.shape, inheriting turtle class into Food.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("SkyBlue")

    def create_food(self):
        """In this we pop up the food any random location on the screen.
        B/w (270, 270) and (-270, -270)"""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
