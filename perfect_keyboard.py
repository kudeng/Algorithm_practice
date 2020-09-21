def isovertwo(s):
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = ''
        d[s[i]] += s[i-1:i]
        d[s[i]] += s[i+1:i+2]
    for k in d:
        s = set(d[k])
        if len(s)>2:
            return False
    return True


def isduichen(s):
    rs = s[::-1]
    if rs==s:
        return True
    else:
        return False


def isrepeat(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return True
    return False



num = int(input())
for index in range(num):
    s = input()
    l = len(s)
    isok = True
    alpha = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    alphalist = alpha.split(' ')
    for i in range(l):
        for j in range(i+1, l):
            if s[j] == s[i]:
                if not isduichen(s[i+1:j]):
                    isok = False
                    break
                break
    if not isovertwo(s):
        isok = False
    if isok:
        print('YES')
        dct = {}
        for ch in s:
            if ch not in dct:
                dct[ch] = 1
            else:
                dct[ch] += 1
        n = len(dct)
        result = ''
        for i in range(l-n+1):
            subs = s[i:i+n]
            if not isrepeat(subs):
                result = subs
                print(subs)
                break
        for ch in result:
            pos = alphalist.index(ch)
            del alphalist[pos]
        print(result + ''.join(alphalist))
    else:
        print('NO')

