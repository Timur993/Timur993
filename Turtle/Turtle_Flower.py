import turtle
turtle.speed(5)
d = 3
def circle():
    turtle.circle(60)
    turtle.circle(-60)
    turtle.right(120)

while d != 0:
    circle()
    d -= 1
