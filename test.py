file = '/Users/kudengma/Desktop/darling.txt'
f = open(file, 'r')
content = f.read()
words = content.split(' ')
d = {}

def sort_by_value(d):
    items=d.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()
    return [ backitems[i][1] for i in range(0,len(backitems))]

for word in words:
    while not word[-1].isalpha():
        word = word[:-2]
    while not word[0].isalpha():
        word = word[1:]
    word = word.lower()
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
s = d.keys()
num = len(s)
lst = sort_by_value(d)
print('共有{}个不同的词汇，排在前13的如下： '.format(num))
for i in range(13):
    j = num - i - 1
    print("{}: {}".format(lst[j], d[lst[j]]))

