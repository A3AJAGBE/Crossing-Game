from turtle import Turtle
COLORS = ["medium spring green", "light sea green", "pink", "pale violet red", "medium purple", "light salmon",
          "pale green", "pale turquoise"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Obstacle():

    def __init__(self):
        self.obstacles = []
        self.posY = -220
        self.generate()

    def generate(self):
        for color in COLORS:
            obstacle = Turtle("circle")
            obstacle.penup()
            obstacle.color(color)
            obstacle.goto(380, self.posY)
            self.posY += 60
            self.obstacles.append(obstacle)

