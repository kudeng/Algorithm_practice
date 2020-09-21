"""
ID: kudengt2
LANG: PYTHON3
TASK: transform
"""
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
def transform(l):
    newl = list(zip(*l))
    for i in range(len(newl)):
        newl[i] = list(newl[i])
    return newl

def reverse(l):
    return l[::-1]

def reverse_each_line(l):
    newl = []
    for line in l:
        newl.append(line[::-1])
    return newl

n = int(fin.readline())
ori = []
dest = []
for i in range(n):
    ori.append(list(fin.readline().strip('\n')))
for i in range(n):
    dest.append(list(fin.readline().strip('\n')))

if reverse_each_line(transform(ori)) == dest:
    ret = '1\n'
elif reverse_each_line(reverse(ori)) == dest:
    ret = '2\n'
elif transform(reverse_each_line(ori)) == dest:
    ret = '3\n'
elif reverse_each_line(ori) == dest:
    ret = '4\n'
elif reverse(ori) == dest:
    ret = '5\n'
elif transform(ori) == dest:
    ret = '5\n'
elif transform(reverse_each_line(reverse(ori))) == dest:
    ret = '5\n'
elif ori == dest:
    ret = '6\n'
else:
    ret = '7\n'
fout.write(ret)






fin.close()
fout.close()