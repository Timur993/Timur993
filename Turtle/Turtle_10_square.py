import turtle
turtle.shape('turtle')
turtle.width(10)
turtle.speed(10)
x = 0
y = 40
def turtle_square(y):
    for i in range(4):
        turtle.forward(y)
        turtle.left(90)
    turtle.penup()
    turtle.right(135)
    turtle.forward(28.28)
    turtle.left(135)
    turtle.pendown()
while x != 10:
    turtle_square(y)
    x+=1
    y+=40

