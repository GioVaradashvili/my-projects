import turtle

def draw_iphone():

    turtle.speed(1)
    turtle.pensize(3)

    turtle.penup()
    turtle.goto(-100, -200)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
    turtle.end_fill()

    # Draw the screen
    turtle.penup()
    turtle.goto(-90, -190)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(180)
        turtle.left(90)
        turtle.forward(360)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.fillcolor("gray")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

draw_iphone()
