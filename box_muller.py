import random
import turtle
import math
import matplotlib.pyplot as figure

#---Uniform---
loc1 = []
n = int(input())

for i in range(1, n + 1):
    n1 = random.random()
    n2 = random.random()
    loc1.append((n1, n2))

turtle.setup(550, 550)
turtle.screensize(500, 500)

turtle.shape('turtle')
turtle.pencolor('black')
turtle.penup()
turtle.hideturtle()
turtle.turtlesize(1, 1, 1)

scale = 100
for x, y in loc1:
    turtle.goto((x - 0.5) * scale * 2, (y - 0.5) * scale * 2)
    turtle.dot()

turtle.done()

# # ------------------ Box-Muller
def box_muller():
    u1 = random.random()
    u2 = random.random()
    z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
    return z0, z1  # Dua angka acak Gaussian

loc2 = []
n = int(input())

for i in range(1, (n + 1)):
    z0, z1 = box_muller()
    loc2.append((z0, z1))

turtle.setup(550, 550)
turtle.screensize(500, 500)

turtle.shape('turtle')
turtle.pencolor('black')
turtle.penup()
turtle.hideturtle()
turtle.turtlesize(1, 1, 1)

scale = 100  
for x, y in loc2:
    turtle.goto(x * scale, y * scale)
    turtle.dot()

figure.plot(loc1, 'ro')
figure.xlabel('Jumlah Data')
figure.ylabel('Distribusi Data')
figure.show()


figure.plot(loc2, 'ro')
figure.xlabel('Jumlah Data')
figure.ylabel('Distribusi Data')
figure.show()

