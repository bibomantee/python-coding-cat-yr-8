import turtle
import random

#[-------- Determining the values --------]
level = int(input("tree level "))
angle = int(input("length pixels "))
length = int(input("angle between branches "))
scale = float(input("scale size "))

#{-------- Turtle setup and settings --------]
screen = turtle.Screen()
screen.setup(width=800, height=600)


t = turtle.Turtle()
t.left(90)
t.speed(0)
t.pensize(2)
t.hideturtle()

t.penup()
t.goto(0, -100)
t.pendown()
#[-------- fractal tree random ---------]

def randomfractaltree(n, length, angle, scale):

    if n == 0:
        return
    
    t.forward(length)
    
    
    angle_variation = angle * 0.20
    scale_variation = scale * 0.90
    
    
    random_angle_left = angle / 2 + (random.random() - 0.5) * angle_variation
    random_scale_left = scale + (random.random() - 0.5) * scale_variation
    random_scale_left = max(0.5, min(0.9, random_scale_left))
    
    
    t.left(random_angle_left)
    randomfractaltree(n - 1, length * random_scale_left, angle, scale)
    t.right(random_angle_left)
    
    
    random_angle_right = angle / 2 + (random.random() - 0.5) * angle_variation
    random_scale_right = scale + (random.random() - 0.5) * scale_variation
    random_scale_right = max(0.5, min(0.9, random_scale_right))
    
    
    t.right(random_angle_right)
    randomfractaltree(n - 1, length * random_scale_right, angle, scale)
    t.left(random_angle_right)
    
    
    t.backward(length)


print(f"Drawing tree")

#[-------- Randomness ---------]

turtle.tracer(0,0)
randomfractaltree(level, length, angle, scale)
turtle.update()
turtle.done()