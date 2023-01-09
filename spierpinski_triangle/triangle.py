import turtle
import random
import math
from datetime import datetime
from PIL import Image
colors = ["blue","red","green","yellow","brown","orange"]
LENGTH = 700
x0 =  - LENGTH / 2
x1 =  LENGTH / 2
y0 = -LENGTH / 2 + 40
top_y = math.sqrt(LENGTH**2 - LENGTH**2/4) + 40
triangle = [(x0,y0),(x1,y0),((x0+x1)/2, y0 + top_y)]

def draw_dot(coord,i=0, size=1):
    turtle.penup()
    turtle.goto(coord)
    turtle.pendown()
    turtle.dot(size)

for point in triangle:
    turtle.color("blue")
    draw_dot(point,0,3)
turtle.color("black")

turtle.speed(10)
x = (x0+x1)/2
y = random.uniform(0,top_y)
i = 0
while i >= 0:
    draw_dot((x,y), i)
    sommet = triangle[random.randint(0,2)]
    x = (x + sommet[0]) / 2
    y = (y + sommet[1]) / 2
    date = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    i += 1
    if i % 500 == 0:
        fileName = 'rendus/rendu-' + str(i)
        turtle.getscreen().getcanvas().postscript(file= fileName+'.eps')
        img = Image.open(fileName + '.eps')
        img.save(fileName + '.jpg')
