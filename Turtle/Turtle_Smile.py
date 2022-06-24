import turtle

turtle.speed(2)
turtle.width(3)


def square():
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()


def eyes():
    turtle.color('blue')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()


def nose():
    turtle.color('black')
    turtle.width(10)
    turtle.right(90)
    turtle.forward(25)


def smile():
    turtle.color('red')
    turtle.width(10)
    turtle.circle(40,180)


def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def main():
    square()
    goto(-40, 110)
    eyes()
    goto(40, 110)
    eyes()
    goto(0, 90)
    nose()
    goto(-40, 50)
    smile()


main()
