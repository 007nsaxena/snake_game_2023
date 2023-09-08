import turtle
from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
score = Score()
screen.title(f'Snake Game')
screen.tracer(0)

t = Turtle()
snake = Snake()
food = Food()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move_snake()
    snake.check_wall()
    snake.check_snake()

    if snake.head.distance(food) < 15:
        food.new_location()
        score.score_up()
        snake.add_snake()

    if snake.hit_wall:
        game_is_on = False
        wall_message = f'You hit the wall. Your score was {score.score}.'
        turtle.color('white')
        turtle.write(wall_message, 'False', 'center', ('Arial', 30))
    if snake.hit_snake:
        game_is_on = False
        snake_message = f'You hit yourself. Your score was {score.score}.'
        turtle.color('white')
        turtle.write(snake_message, 'False', 'center', ('Arial', 30))


screen.exitonclick()
