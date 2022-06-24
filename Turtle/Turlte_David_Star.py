import turtle
turtle.shape("turtle")
turtle.shapesize(1)
turtle.color("green", "yellow")
turtle.speed(10)
for step in range(6):
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(50)
        turtle.left(120)
    turtle.end_fill()
    turtle.forward(50)
    turtle.right(60)

turtle.hideturtle()