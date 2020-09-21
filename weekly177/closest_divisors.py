def divisors(num):
    import math
    mid = math.sqrt(num)
    if mid % 1 == 0:
        return (mid, mid)
    for i in range(math.floor(mid), 0, -1):
        if num % i == 0:
            return (i, num / i)


num = 8
(x1, x2) = divisors(num+1)
(y1, y2) = divisors(num+2)
gap1 = x2-x1
gap2 = y2-y1
res = []
if gap2>gap1:
    res.append(x1)
    res.append(x2)
else:
    res.append(y1)
    res.append(y2)
print(res)