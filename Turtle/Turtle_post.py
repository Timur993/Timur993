A = []
for i in range(8):
    a = int(input())
    A.append(a)
if A[0] + A[2] + A[4] > A[6]:
    print('NO')
elif A[1] + A[3] > A[7]:
    print('NO')
elif A[1] + A[5] > A[7]:
    print('NO')
else:
    print('YES')
