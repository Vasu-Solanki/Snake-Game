from turtle import Turtle

# Set the 3 blocks or part of the snake one another.
snake_position = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# TODO 1: CREATING A SNAKE BODY.
class Snake:

    def __init__(self):
        # It collects the every square memory in variable.
        # For "self." It helps us to call the snake_body everywhere in this file.
        self.snake_body = []
        self.creating_body()
        # Giving the snake head as a triangle.
        self.face = self.snake_body[0].shape("triangle")
        self.face_color = self.snake_body[0].color("maroon")
        self.head = self.snake_body[0]

    # Creating the snake body.
    def creating_body(self):
        for position in snake_position:
            self.create_parts(position)

    def create_parts(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("olive")
        snake.turtlesize()
        snake.goto(position)
        self.snake_body.append(snake)

    def add_new_part(self):
        self.create_parts(self.snake_body[-1].position())

    # TODO 2: MOVING AND CONTROLLING THE SNAKE.
    def move(self):
        # In this we are reversing the loop like --> 5,4,3,2,1,0.
        # In range (last element, 1st element, help us to go last - 1st) of snake_body.
        for part_num in range(len(self.snake_body) - 1, 0, -1):
            # Snake_body[last 2nd element]. x-axis coordinate.-->(new_x,0)
            new_x = self.snake_body[part_num - 1].xcor()
            # Snake_body[last 2nd element]. y-axis coordinate.-->(0,new_y)
            new_y = self.snake_body[part_num - 1].ycor()
            # In this the last element goto the position of the last 2nd element and so on.
            # Snake_body[part_num] = last element, goto(new_x, new_y) = 2nd last element position.
            self.snake_body[part_num].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.head.setheading(90)
            # This will help to stop the snake move from distance 10.
            # BUG FIXED.
            # self.head.forward(20)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.head.setheading(270)
            # self.head.forward(20)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.head.setheading(0)
            # self.head.forward(20)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.head.setheading(180)
            # self.head.forward(20)
