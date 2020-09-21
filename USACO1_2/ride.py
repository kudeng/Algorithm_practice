"""
ID: kudengt2
LANG: PYTHON3
TASK: ride
"""
def findgroup(str):
    product = 1
    for ch in str:
        product = product * (ord(ch) - 64)
        product = product % 47
    return product


fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
comet = fin.readline()
group = fin.readline()
if findgroup(comet) == findgroup(group):
    fout.write('GO\n')
else:
    fout.write('STAY\n')
fin.close()
fout.close()