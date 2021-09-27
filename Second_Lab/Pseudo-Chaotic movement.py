from random import *
import turtle
import math

turtle.shape('turtle')
turtle.speed(0)
while True:
    turtle.forward(random() * 40)
    if (random()) >= 0.5:
        turtle.right(random() * 180)
    else:
        turtle.left(random() * 180)
