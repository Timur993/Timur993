import turtle
turtle.shape('turtle')
n = 0
def spider_legs():
    turtle.forward(100)
    turtle.stamp()
    turtle.goto(0,0)
    turtle.right(360/12)

while n!= 12:
    spider_legs()
    n+=1

