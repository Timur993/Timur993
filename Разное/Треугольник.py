a = int(input(''))
b = int(input(''))
c = int(input(''))


if a==b==c:
    print('acute')

if c>a>b:
    if c*c>a*a+b*b:
        print('obtuse')
    if c*c<a*a+b*b:
        print('acute')
    if c*c==a*a+b*b:
        print('right')
    else:
        print('impossible')

if a>c>b:
    if a*a>c*c+b*b:
        print('obtuse')
    if a*a<c*c+b*b:
        print('acute')
    if a*a==c*c+b*b:
        print('right')
    else:
        print('impossible')

if b>c>a:
    if b*b>c*c+a*a:
        print('obtuse')
    if b*b<c*c+a*a:
        print('acute')
    if b*b==c*c+a*a:
        print('right')
    else:
        print('impossible')