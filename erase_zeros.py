n = int(input())
for i in range(n):
    s = input()
    s = s.strip('0')
    count = 0
    for ch in s:
        if ch == '0':
            count += 1
    print(count)