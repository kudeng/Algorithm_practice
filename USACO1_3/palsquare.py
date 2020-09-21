"""
ID: kudengt2
LANG: PYTHON3
TASK: palsquare
"""
fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')
alpha = '0123456789ABCDEFGHIJ'

def to_base_n(num, base):
    global alpha
    s = ''
    while num!=0:
        s += alpha[num % base]
        num = num // base
    return s[::-1]


n = int(fin.readline())
result = []
for i in range(1, 301):
    s = to_base_n(i*i, n)
    if s == s[::-1]:
        result.append('{} {}'.format(to_base_n(i, n), s))
fout.write('\n'.join(result) + '\n')




fin.close()
fout.close()