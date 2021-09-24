from random import *
import turtle
import math



number_of_turtles = int(input())
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

for i in range(1, 5):
    turtle.forward(400)
    turtle.left(90)

turtle.hideturtle()


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.right(randint(-180, 180))
    unit.shapesize(0.5, 0.5, 1)


while True:
    for unit in pool:
        if unit.xcor() - 200 > 0:
            unit.left(180 - 2 * unit.heading())
        if unit.xcor() + 200 < 0:
            unit.left(180 - 2 * unit.heading())
        if unit.ycor() - 200 > 0:
            unit.right(unit.heading() * 2)
        if unit.ycor() + 200 < 0:
            unit.right(unit.heading() * 2)

        unit.forward(5)
