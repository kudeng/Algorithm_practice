"""
ID: kudengt2
LANG: PYTHON3
TASK: crypt1
"""
from itertools import product
fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')

n = int(fin.readline())
line = fin.readline()
l = list(map(int, line.split(' ')))
l_str = line.strip('\n').split(' ')
def check(num, length):
    s = str(num)
    global l_str
    if len(s) != length:
        return False
    for ch in s:
        if ch not in l_str:
            return False
    return True


count = 0
for a,b,c,d,e in product(l,l,l,l,l):
    top = a*100 + b*10 + c
    if not check(top*d, 3):
        continue
    if not check(top*e, 3):
        continue
    if not check(top*d*10+top*e, 4):
        continue
    count += 1
    # print('{} {} {} {} {}'.format(a,b,c,d,e))
# print(count)
fout.write(str(count) + '\n')

fin.close()
fout.close()