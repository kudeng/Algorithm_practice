"""
ID: kudengt2
LANG: PYTHON3
TASK: combo
"""
fin = open('combo.in', 'r')
fout = open('combo.out', 'w')
n = int(fin.readline())
famer = list(map(int, fin.readline().split(' ')))
maker = list(map(int, fin.readline().split(' ')))

def check(x, y, n):
    l = list(range(1, n + 1))
    t = list(range(1, n))
    lock = l + t
    # print(lock)
    gap = min(abs(lock.index(x)-lock.index(y)),
            abs(lock.index(x, n-1)-lock.index(y)),
            abs(lock.index(x)-lock.index(y, n-1))
            )
    if gap > 4:
        return 0
    else:
        return 5-gap

product = 1
for i,j in zip(famer, maker):
    product *= check(i, j, n)
result = 250 - product
if n < 5:
    result = pow(n, 3)
fout.write(str(result)+'\n')



fin.close()
fout.close()