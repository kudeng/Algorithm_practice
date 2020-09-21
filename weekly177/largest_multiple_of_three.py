digits = [1,2,1,4,5,6,3]
d = {}
for i in digits:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d[1])