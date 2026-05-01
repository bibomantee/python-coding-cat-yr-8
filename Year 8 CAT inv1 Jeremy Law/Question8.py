import turtle

#[-------- Values --------]
n = 8
length = 100
angle  = 30
scale  = 0.75

#[-------- Fractal Tree --------]

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

#[-------- Turtle Settings --------]
turtle.tracer(False)
turtle.speed(0)
turtle.penup()
turtle.goto(0, -200)
turtle.setheading(90)
turtle.pendown()

fractaltree(n, length, angle, scale)

#[-------- Ending the tree, im using a different once because the old one was weird ---------]

turtle.exitonclick()
