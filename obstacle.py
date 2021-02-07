from turtle import Turtle
import random

COLORS = ["medium spring green", "light sea green", "pink", "pale violet red", "medium purple", "light salmon",
          "pale green", "pale turquoise"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Obstacle:

    def __init__(self):
        self.obstacles = []

    def generate(self):
        # To prevent the obstacle from cluster
        num = random.randint(1, 4)
        if num == 1:
            obstacle = Turtle("circle")
            obstacle.shapesize(stretch_wid=1, stretch_len=2)
            obstacle.penup()
            obstacle.color(random.choice(COLORS))
            posY = random.randint(-220, 220)
            obstacle.goto(400, posY)
            self.obstacles.append(obstacle)

    def move_obstacle(self):
        for ball in self.obstacles:
            ball.backward(STARTING_MOVE_DISTANCE)

