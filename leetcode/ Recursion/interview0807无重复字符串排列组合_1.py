'''
author: 马天骁
date:   2020-5-8
source: leetcode 面试题0807 无重复字符串排列组合 解法一
idea:   创建所有abc的排列，在每个可能的位置上插入d
'''
class Solution:
    def permutation(self, S: str) -> List[str]:
        if len(S)==0:
            return []
        res = []
        res.append(S[0])
        for ch in S[1:]:
            length = len(res)
            S_len = len(res[0])
            for i in range(length):
                for j in range(S_len+1):
                    res.append(res[i][:j] + ch + res[i][j:])
            res = res[i+1:]
        return res