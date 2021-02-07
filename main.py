from turtle import Screen
from player import Player
from obstacle import Obstacle
from scoreboarad import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("ivory")
screen.title("A3AJAGBE Crossing Game")
screen.tracer(0)

player = Player()
obstacle = Obstacle()
scoreboard = Scoreboard()

# Moving the turtle
screen.listen()
screen.onkey(player.move, "Up")

# The game application
start = True
while start:
    time.sleep(0.1)
    screen.update()

    obstacle.generate()
    obstacle.move_obstacle()

    # Detect collision with obstacles
    for ball in obstacle.obstacles:
        if ball.distance(player) < 25:
            start = False
            scoreboard.game_over()

    # Detects when the player cross the screen successfully
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.default_position()
        obstacle.increase_speed()

# Close only when exited
screen.exitonclick()
