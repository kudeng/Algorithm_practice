"""
ID: kudengt2
LANG: PYTHON3
TASK: friday
"""
def isleap(y):
    return y%400==0 or y%4==0 and y%100!=0


def add_days(y, m):
    d_in_m = [-1, 3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    return d_in_m[m] + (m == 2 and isleap(y))


fin = open('friday.in', 'r')
fout = open('friday.out', 'w')
n = int(fin.readline())
num = [0, 0, 0, 0, 0, 0, 1]
week = 6
for y in range(1900, 1900+n):
    for m in range(1, 13):
        week = (week + add_days(y, m)) % 7
        num[week] += 1
num[week] -= 1

num_of_sat = num[6]
for i in range(6, 0, -1):
    num[i] = num[i-1]
num[0] = num_of_sat
newlist = map(str, num)
fout.write(' '.join(newlist) + '\n')



fin.close()
fout.close()