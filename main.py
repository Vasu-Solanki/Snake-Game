from scoreboard import ScoreBoard
from turtle import Screen
from snake import Snake
import time
from food import Food

# TODO--> SETTING THE SCREEN.

# initializing the screen for the game.
screen = Screen()

# Set the size of the window screen.
screen.setup(height=600, width=600)

# Set background color for the window screen.
screen.bgcolor("black")

# Giving the title name to the window screen.
screen.title("Snake Game")

# Stopping the animation created when the square move.
screen.tracer(0)

# This will help us to control the snake.
snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

# In this we give color and size to the food.
food = Food()

#
score_board = ScoreBoard()

# It's help us to loop in the while loop.
snake_alive = True

# In this we move the snake until it dies.
while snake_alive:
    # We can use this as a speed slow or fast for the snake.
    screen.update()
    time.sleep(0.1)
    snake.move()
    # if the distance b/w snake head and food are smaller than 20, then this will execute.
    if snake.head.distance(food) < 20:
        food.create_food()
        snake.add_new_part()
        score_board.current_score()
    # if the snake collides with the wall or go beyond 300 from the origin ain any direction then the game is over.
    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        score_board.game_over()
        snake_alive = False
    # Here we're using the slicing of the list aka snake_body.
    for parts in snake.snake_body[1:]:
        if snake.head.distance(parts) < 10:
            score_board.game_over()
            snake_alive = False


# this will allow us to exit the window screen by click and also help to see the result.
screen.exitonclick()
