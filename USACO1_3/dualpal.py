"""
ID: kudengt2
LANG: PYTHON3
TASK: dualpal
"""
fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')
def to_base_n(num, base):
    s = ''
    while num!=0:
        s += str(num % base)
        num = num // base
    return s[::-1]


n, min_num = map(int, fin.readline().split(' '))
result = []
total = 0
for i in range(min_num+1, 20000):
    count = 0
    for j in range(2, 11):
        s = to_base_n(i, j)
        if s == s[::-1]:
            count += 1
            if count > 1:
                break
    if count > 1:
        result.append(str(i))
        total += 1
        if total == n:
            break
fout.write('\n'.join(result) + '\n')


fin.close()
fout.close()