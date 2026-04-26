import turtle
#create turtle screen and set background colour
screen=turtle.Screen()
screen.bgcolor("White")
# create a turtle object to draw with
pen=turtle.Turtle()
# set colour of the turtle
pen.color("Blue")
# set speed of the turtle
pen.speed(2)
# draw line of length 20 pixels
pen.forward(20)
# rotate the turtle 90 degrees to the right to
# change the direction it’s about to draw in
pen.right(90)
# draw the other 3 sides of a rectangle
pen.forward(40)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(40)
#hide turtle
pen.hideturtle()
#keep turtle window open when done
turtle.done()

def tree(n):
    if n == 0:
        return
    turtle.forward(50)
    
    pos = turtle.position()
    heading = turtle.heading()
    turtle.left(30)
    tree(n-1)
    turtle.setposition(pos)
    turtle.setheading(heading)
    turtle.right
    tree(n-1)
    turtle.setposition(pos)
    turtle.setheading(heading)
    turtle.backward(50)
    
def draw_tree(level, x_offset):
    turtle.penup()
    turtle.goto(x_offset, -200)
    turtle.pendown()
    turtle.setheading(90)
    tree(level)

turtle.speed(0)
turtle.hideturtle()

draw_tree(5, -100)

turtle.done()