import random
import time
import turtle
import math

def box_muller():
    u1 = random.random()
    u2 = random.random()
    z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
    return z0, z1  # Dua angka acak Gaussian

loc = []
n = int(input())

for i in range(1, (n + 1)):
    z0, z1 = box_muller()
    loc.append((z0, z1))
    print('({}, {})'.format(z0, z1))
    time.sleep(0.01)

turtle.setup(550, 550)
turtle.screensize(500, 500)

turtle.shape('turtle')
turtle.pencolor('black')
turtle.penup()
turtle.hideturtle()
turtle.turtlesize(1, 1, 1)

scale = 100  # adjust as needed. This is for visualising  Box-Muller data so that the turtle can go far.
for x, y in loc:
    turtle.goto(x * scale, y * scale)
    turtle.dot()

turtle.done()

# ------------------------------------------------
