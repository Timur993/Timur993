import random

count = int(input('Сколько раз подбросим монетку? '))
heads = 0
tails = 0

while count != 0:
    x = random.randint(1,2)
    if x == 1:
        heads+=1
        count-=1
    elif x == 2:
        tails+=1
        count-=1
if heads > tails:
    print('Победил орёл, он выпал', heads,'раз')
else:
    print('Победила решка, она выпала', tails,'раз')