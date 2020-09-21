"""
ID: kudengt2
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
n = int(fin.readline())
d = {}
namelist = []
for i in range(n):
    name = fin.readline()
    namelist.append(name)
    d[name] = 0
for i in range(n):
    name = fin.readline()
    total, recv = map(int, fin.readline().split(' '))
    if recv != 0:
        d[name] -= total
        d[name] = d[name] + (total % recv)
        for j in range(recv):
            recver = fin.readline()
            d[recver] += total // recv
for name in namelist:
    strip_name = name.strip('\n')
    fout.write('{} {}\n'.format(strip_name, d[name]))




fin.close()
fout.close()