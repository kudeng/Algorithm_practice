"""
ID: kudengt2
LANG: PYTHON3
TASK: milk2
"""
fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')
n = int(fin.readline())
num = [-1]
min_start = 1000000
for i in range(n):
    start, end = map(int, fin.readline().split(' '))
    if start < min_start:
        min_start = start
    if end > len(num):
        num += [0]*(end-len(num))
    num[start+1:end+1] = [1]*(end-start)
max_itval = 0
max_none = 0
temp_max = 0
temp_none = 0
flag = num[1]
num[min_start] = num[min_start+1]
for i in range(min_start+1, len(num)):
    if num[i]==1 and num[i]==num[i-1]:
        temp_max += 1
    elif num[i]==0 and num[i]==num[i-1]:
        temp_none += 1
    elif num[i]==1 and num[i]!=num[i-1]:
        if temp_none > max_none:
            max_none = temp_none
        temp_none = 0
        temp_max = 1
    else:
        if temp_max > max_itval:
            max_itval = temp_max
        temp_none = 1
        temp_max = 0
if temp_max > max_itval:
    max_itval = temp_max
if temp_none > max_none:
    max_none = temp_none
fout.write(f'{max_itval} {max_none}\n')



fin.close()
fout.close()