def minWindow(s: str, t: str) -> str:
    key = ''
    key_index = []
    dict_t = {}
    print(key)
    for ch in t:
        if ch not in dict_t:
            dict_t[ch] = 1
        else:
            dict_t[ch] += 1
    for i, ch in enumerate(s):
        if ch in t:
            key += ch
            key_index.append(i)
    def isin(chars):
        dict_ch = {}
        for ch in chars:
            if ch not in dict_ch:
                dict_ch[ch] = 1
            else:
                dict_ch[ch] += 1
        for ch in dict_t:
            if ch not in dict_ch or dict_ch[ch] < dict_t[ch]:
                return False
        return True
    search_len = len(t)
    min_length = len(s) + 1
    res = (-1, -1)
    while search_len <= len(key):
        for i in range(len(key) - search_len+1):
            if isin(key[i:i + search_len]):
                length = key_index[i + search_len - 1] - key_index[i]
                print(key[i:i + search_len])
                if length < min_length:
                    min_length = length
                    res = (key_index[i], key_index[i + search_len - 1])
        search_len += 1
    return s[res[0]:res[1] + 1]

s = "ueeouptjcosytyujjcvnmtndauseqxvkdzayrtjvhdtcbnnmrjbfeokfkdjacgnhfnhwjqtsumvvckkvtlbaclfmqqpuwecdtjccavxwiutmedhapkarwhfozwlxapauyeyaavwkpswwvdwmqydoflcejpbkedgdieficeutwqrtvnglllzswewgtzsadydlekvgqpcmhtgejmqwxrpwxletnwtquybakyjbnlnuevynjqmjkbfjojcbhxrdvudismjhxybeuctdsfoegtoxesylqsonouvhgeqgdsmzwfeontvvojstbtgrlxhzrcixjzfmtrnpzrfomalbjeunzcemzllqqwqzxxnqpahqtmggprhyxdlwfsiffwxvspwrnjheloufccnrtusrzfpexalfwjcqyzhnkqrygnfipsclmuclbtrztdgroihojqcwgvumjzxarblfxpsyjjxeofwcqftzwvvesrrbsqcjrpqofimqsmuitsljyejubgytarxsjbecqusxdhnxvifoasyayjwbrxvtoumaxsenmxlrgaqbiyrlqrlraksuhppxjdxgvcwibjbhjukusbfitsbveupljhjvkgdgkzqnirwulgofivqbprwulofvvoshxvnjvdzfxvzkcnqmkgnazlulbbiyqagpvvaszzyyvxkxncjxkyzklvvnxfnpfvearetsgtsbscafflfrlgbwcylzdboiwulnagfgzxhrcjzjugafmceocrpgsdqpzbcahkggjoalzzuuhxbtzfkdxzjpdagcdlenxltgbvuawqwdnyxofhsegdulfcqjnuwkhrtinnljdhptfmhlvbpdflpkqhtddrqljjtywejb"

t = "oyutmeghfylklcvbjqfmkxx"
print(minWindow(s, t))