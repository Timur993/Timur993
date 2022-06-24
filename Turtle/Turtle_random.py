import random
import turtle


turtle.speed(10)

for i in range(random.randint(10,200)):
    turtle.forward(random.randint(1,50))
    turtle.right(random.randint(1,360))

