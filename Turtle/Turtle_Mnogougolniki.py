import turtle
turtle.speed(1)
x = 30
n = 3
def huy():
    for i in range(n):
        turtle.left(360/n)
        turtle.forward(x)
    turtle.left(90)
    turtle.forward(5)
    turtle.right(45)

while n!=7:
    huy()
    x+=20
    n+=1

