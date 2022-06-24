import turtle
x = 1
turtle.speed(20)
turtle.width(3)
turtle.shape('turtle')
def spiral():
    for i in range(40):
        turtle.right(5)
        turtle.forward(x)

while True:
    spiral()
    x+=1