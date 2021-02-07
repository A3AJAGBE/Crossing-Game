from turtle import Screen
from player import Player
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("ivory")
screen.title("A3AJAGBE Crossing Game")
screen.tracer(0)

player = Player()

# Moving the turtle
screen.listen()
screen.onkey(player.move, "Up")

# The game application
start = True
while start:
    time.sleep(0.1)
    screen.update()


# Close only when exited
screen.exitonclick()
