"""
ID: kudengt2
LANG: PYTHON3
TASK: barn1
"""
fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')

boards, stalls, n = map(int, fin.readline().split(' '))
barns = [0] * stalls
for i in range(n):
    barns[int(fin.readline())-1] = 1
gaps = []
first_stall = barns.index(1)
last_stall = len(barns) - 1 - barns[::-1].index(1)
temp_gap = 0
for i in range(first_stall, last_stall+1):
    if barns[i] == 0:
        temp_gap += 1
    else:
        gaps.append(temp_gap)
        temp_gap = 0
gaps.sort(reverse=True)
if boards > len(gaps):
    result = n
else:
    result = last_stall - first_stall + 1
    for i in range(boards-1):
        result -= gaps[i]
fout.write(str(result) + '\n')


fin.close()
fout.close()