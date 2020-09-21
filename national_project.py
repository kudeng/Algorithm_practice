from math import ceil

num = int(input())
for i in range(num):
    s = input()
    l = s.split(" ")
    n = int(l[0])
    g = int(l[1])
    b = int(l[2])
    days = ceil(n/2)
    if days/g <= 1:
        print(n)
    elif n/g<1 and n%g<days:
        print(n)
    else:
        t = ceil(days/g) - 1
        result = t*b + days
        if result < n:
            print(n)
        else:
            print(result)

