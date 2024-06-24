from turtle import Turtle, Screen
import random

# tim´s full name
timothy_the_third = Turtle()

# friends call him "tim"
tim = timothy_the_third

# general tim´s characteristics
tim.shape("turtle")
tim.color("green")
tim.pensize(1)

# and screen configuration
screen = Screen()
screen.colormode(255)
screen.screensize(2000, 1500)
screen.delay(0)

# ----- returns a random pallete of R, G, B colors --------


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_number = (r, g, b)
    return random_number

# -------- get the turtle to do a spirograph  ----------


def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap )):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + size_of_gap)


spirograph(10)

# -------- get the turtle to do a random walk simulation -----------


def random_walk():
    angles = [0, 90, 180, 270]

    for i in range(200):
        steps = 10
        tim.pencolor(random_color())
        angle = random.choice(angles)
        tim.setheading(angle)
        tim.fd(steps)


# ----  starting from a triangle draw the next shape increasing 1 corner ------
# ------------- i.e. triangle, square, pentagon, hexagon etc... ---------------

def geometric_shapes():
    number = 2
    for _ in range(6):
        tim.pencolor(random_color())
        number += 1
        degrees = 360 / number
        for _ in range(number):
            tim.forward(100)
            tim.right(degrees)


# ------------  draw dotted line with tim (2 different methods)----------------

# method 1: using penup, pendown function
def dot_line_1():
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


# method 2: coloring the lines black and white every 10 steps alternately.
def dot_line_2():
    for _ in range(10):
        tim.pen(pencolor="black")
        tim.forward(10)
        tim.pen(pencolor="white")
        tim.forward(10)


screen.exitonclick()
