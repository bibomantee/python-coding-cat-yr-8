import turtle

n = int(input("tree level "))
length = int(input("length "))
angle  = int(input("angle "))
scale  = int(float(input("scale ")))

from numpy import angle

def fractaltree(n, length, angle, scale):
     if n == 0:
        return
    
turtle.forward(length)
turtle.left(angle)
fractaltree(n - 1, length * scale, angle, scale)
turtle.right(2 * angle)
fractaltree(n - 1, length * scale, angle, scale)
turtle.left(angle)
turtle.backward(length)

turtle.speed(0)
turtle.left(90)
turtle.penup()
turtle.goto(0, -200)
fractaltree

turtle.done()
