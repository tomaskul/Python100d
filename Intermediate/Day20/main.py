from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

game_is_on = True
def stop_game():
    global game_is_on
    game_is_on = False

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(stop_game, "Escape")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision.
    if snake.head.distance(food) < 15:
        #print("nom nom nom..")
        food.refresh()
        scoreboard.increment_score()

    # Detect wall collision.
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()



screen.exitonclick()