T = int(input())
for t in range(T):
    n = int(input())
    prince = [0]+[1]*n
    unmarried = 0
    for i in range(1, n+1):
        princess = list(map(int, input().split()))
        del princess[0]
        if unmarried:
            continue
        princess.sort()
        # print(princess)
        flag = False
        for v in princess:
            if prince[v]:
                prince[v] = 0
                flag = True
                break
        # print(i)
        # print(flag)
        if not flag:
            unmarried = i
    if not unmarried:
        print('OPTIMAL')
    else:
        print('IMPROVE')
        print(f'{unmarried} {prince.index(1)}')

