"""
ID: kudengt2
LANG: PYTHON3
TASK: milk
"""
fin = open('milk.in', 'r')
fout = open('milk.out', 'w')


class famer(object):
    def __init__(self, p, o):
        self.price = p
        self.out = o

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price



needs, n = map(int, fin.readline().split(' '))
famer_list = []
for i in range(n):
    p, o = map(int, fin.readline().split(' '))
    famer_list.append(famer(p, o))
famer_list.sort()
cost = 0
temp_needs = 0
for f in famer_list:
    if temp_needs >= needs:
        break
    if temp_needs + f.out <= needs:
        cost += f.out * f.price
        temp_needs += f.out
    else:
        cost += f.price*(needs-temp_needs)
        break
fout.write(str(cost) + '\n')


fin.close()
fout.close()