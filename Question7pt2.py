import turtle

def simpletree(n):
    
    if n == 0:
        return

# [--------- Tree drawing ---------]
    turtle.forward(50)
    turtle.left(30)
    simpletree(n - 1)
    turtle.right(60)
    simpletree(n - 1)
    turtle.left(30)
    turtle.backward(50)


# [--------- Test ---------]
turtle.speed(0)         

# [--------- Tree Level 4 ---------]
turtle.penup()
turtle.goto(-700, -150)
turtle.pendown()
simpletree(4)

# [------- Tree Level 6 -------]
turtle.penup()
turtle.goto(-300, -150)
turtle.pendown()
simpletree(6)

# [-------- Tree Level 10 ---------]
turtle.penup()
turtle.goto(400, -150)
turtle.pendown()
simpletree(10)

turtle.done()
# [---------- Running the code ------------]
simpletree