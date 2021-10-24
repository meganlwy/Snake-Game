from turtle import Turtle, Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True

mysnake = Snake()
# mysnake.createsnake()  # don't need because the function will be called at the moment we create a Snake item
myfood = Food()
myscoreboard = Scoreboard()


screen.listen()
screen.onkey(mysnake.up, "Up")
screen.onkey(mysnake.down, "Down")
screen.onkey(mysnake.left, "Left")
screen.onkey(mysnake.right, "Right")

while game_on:
    time.sleep(0.1)
    screen.update()
    mysnake.snakemove()

    # detect collision with food
    if mysnake.head.distance(myfood) < 15:
        myscoreboard.clear()
        myfood.refresh()
        mysnake.extendtail()
        myscoreboard.increasescore()

    # detect collision with wall
    if (
        mysnake.head.xcor() > 280
        or mysnake.head.xcor() < -280
        or mysnake.head.ycor() > 280
        or mysnake.head.xcor() < -280
    ):
        game_on = False
        myscoreboard.endgame()

    # detect collision with tail
    for body in mysnake.snakebody[1:]:
        if mysnake.head.distance(body) < 10:
            game_on = False
            myscoreboard.endgame()

screen.exitonclick()
