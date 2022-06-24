import turtle
turtle.width(3)
x = 10
y = 0
turtle.shape('turtle')
def square_spiral():
    turtle.forward(x)
    turtle.left(90)

while y != 30:
    square_spiral()
    x+=10
    y+=1