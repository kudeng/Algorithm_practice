n = int(input())
for i in range(n):
    m, n = map(int, input().split(' '))
    if m%2 != n%2:
        print('NO')
        continue
    if m >= n*n:
        print('YES')
    else:
        print('NO')