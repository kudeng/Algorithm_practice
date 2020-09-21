"""
ID: kudengt2
LANG: PYTHON3
TASK: namenum
"""
fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')
fs = open('dict.txt', 'r')
valid_name = []
result = []
phone = [-1,
         -1,
         ['A', 'B', 'C'],
         ['D', 'E', 'F'],
         ['G', 'H', 'I'],
         ['J', 'K', 'L'],
         ['M', 'N', 'O'],
         ['P', 'R', 'S'],
         ['T', 'U', 'V'],
         ['W', 'X', 'Y']
]
for line in fs.readlines():
    valid_name.append(line.strip('\n'))
cow_number = list(map(int, list(fin.readline().strip('\n'))))
same_long_valid_name = []
for name in valid_name:
    if len(name) == len(cow_number):
        same_long_valid_name.append(name)
for name in same_long_valid_name:
    flag = True
    for i in range(len(cow_number)):
        if name[i] not in phone[cow_number[i]]:
            flag = False
            break
    if flag:
        result.append(name)
if len(result) == 0:
    fout.write('NONE\n')
else:
    fout.write('\n'.join(result) + '\n')




fs.close()
fin.close()
fout.close()