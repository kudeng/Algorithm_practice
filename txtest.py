s = input()
mid = 0
small = 0
res = 0
for ch in s:
    if ch=='[':
        mid += 1
    elif ch==']':
        if mid > 0:
            mid -= 1
        else:
            res += 1
    elif ch=='(':
        small += 1
    else:
        if small > 0:
            small -= 1
        else:
            res += 1
res += mid
res += small
print(res)