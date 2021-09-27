from random import *
import turtle
import math

file = open('Font.txt')
duniversal = [0] * 10
for i in range(0, 10):
    str = file.readline()
    bigcort = str.split(', ')
    for j in range(0, len(bigcort)):
        bigcort[j] = bigcort[j].split()
        bigcort[j][0] = float(bigcort[j][0])
        bigcort[j][1] = float(bigcort[j][1])
    duniversal[i] = bigcort

turtle.shape('turtle')
turtle.penup()
turtle.goto(turtle.xcor() - 200, turtle.ycor())
turtle.pendown()
len_unit = 50

num = input()
dunit = 0
for i in range(0, len(num)):
    dunit = duniversal[int(num[i])]
    for angle, L in dunit:
        turtle.right(angle)
        turtle.forward(L * len_unit)
    for angle, L in dunit[::-1]:
        turtle.forward(-L * len_unit)
        turtle.right(-angle)
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()
