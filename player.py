from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.left(90)
        self.default_position()

    def move(self):
        """This function moves the turtle up"""
        self.forward(MOVE_DISTANCE)

    def default_position(self):
        self.goto(STARTING_POSITION)
