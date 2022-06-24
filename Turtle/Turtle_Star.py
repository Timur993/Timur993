import turtle

n = int(input('Количество вершин звезды: '))
turtle.speed(5)
turtle.right(180)
def star():
    for x in range(n):
        turtle.forward(150)
        turtle.left(180 - 180/n)


star()

