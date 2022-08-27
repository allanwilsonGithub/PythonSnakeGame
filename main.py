from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from playsound import playsound


screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("#5FAA6F")
screen.title("Allan's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_om = True

while game_is_om:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 490 or snake.head.ycor() < -490:
        game_is_om = False
        scoreboard.game_over()
        playsound('media/sad-game-over-trombone.wav')

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_om = False
            scoreboard.game_over()
            playsound('media/sad-game-over-trombone.wav')


screen.exitonclick()
