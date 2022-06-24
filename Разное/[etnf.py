'''a = int(input(''))
b = int(input(''))
c = int(input(''))


if a==b==c:
    print('acute')
elif c>=a+b or b>=c+a or a>=c+b:
    print('impossible')
elif c>=a and c>=b:
    if c*c==a*a+b*b:
        print('right')
    elif c*c>a*a+b*b:
        print('obtuse')
    elif c*c<a*a+b*b:
        print('acute')
elif a>=b and a>=c:
    if a*a==c*c+b*b:
        print('right')
    elif a*a>c*c+b*b:
        print('obtuse')
    elif a*a<c*c+b*b:
        print('acute')
elif b>=c and b>=a:
    if b*b==c*c+a*a:
        print('right')
    elif b*b>c*c+a*a:
        print('obtuse')
    elif b*b<c*c+a*a:
        print('acute')'''
'''a = []
b = []
max = 0
while a != 0:
    a = int(input())
    b.append(a)
    for i in b:
        if i % 2 == 0 and i>max:
            max = i
print(max)
'''

'''a = int(input())
b = int(input())

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)'''

'''count = int(input())
a = []
while count!=0:
    count-=1
    b = int(input())
    a.append(b)
print(max(a, key=a.count))
'''
'''B = []
MAX = 0
a = int(input())
B.append(a)
for i in range(1000000000):
    a = int(input())
    if a == 0:
        break
    B.append(a)
    if i > 4:
        B.pop(0)
    if B[0] > MAX:
        MAX = B[0]
    i += 1
print(MAX)
'''

'''a = input("").split()
if a[0] and a[1] < a[2]:
    print('YES')
else:
    print('NO')'''

'''n,k = int(input()), int(input())
last = 0
for i in range(1,n+1):
    last = (last + k) % i
print(last)'''

n = int(input())

