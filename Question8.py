import turtle


n = int(input("tree level "))
length = int(input("length pixels "))
angle  = int(input("angle between branches "))
scale  = (float(input("scale or size ")))

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
turtle.penup()
turtle.goto(0, -200)
turtle.setheading(90)
turtle.pendown()

fractaltree(n, length, angle, scale)

turtle.exitonclick()
