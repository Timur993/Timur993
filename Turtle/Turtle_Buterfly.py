import turtle
turtle.speed(5)
x = 20
d = 0
turtle.right(90)
def circle():
    turtle.circle(x)
    turtle.circle(-x)
while d != 10:
    circle()
    d += 1
    x += 10
