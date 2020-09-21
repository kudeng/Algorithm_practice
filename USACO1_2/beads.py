"""
ID: kudengt2
LANG: PYTHON3
TASK: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')
n = int(fin.readline())
necklace = fin.readline().strip('\n')
double_lace = necklace*2

def countside(str, ch):
    count = 0
    for s in str:
        if s==ch or s=='w':
            count += 1
            continue
        else:
            break
    return count

maxnum = 0

# if 'b' not in double_lace or 'r' not in double_lace:
#     maxnum = n
# else:
if True:
    for i in range(len(double_lace)):
        rleft = countside(double_lace[:i][::-1], 'r')
        rright = countside(double_lace[i:], 'r')
        bleft = countside(double_lace[:i][::-1], 'b')
        bright = countside(double_lace[i:], 'b')
        if rleft+bright > rright+bleft:
            temp = rleft + bright
        else:
            temp = rright + bleft
        if temp > maxnum:
            maxnum = temp

if maxnum > n:
    maxnum = n



fout.write(str(maxnum) + '\n')



fin.close()
fout.close()