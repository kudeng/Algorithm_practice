'''
author: 马天骁
date:   2020-5-8
source: leetcode 面试题0807 无重复字符串排列组合 解法二
idea:   要生成abcd的全排列，则可将a b c d分别作为首字母，再加上其他字母的全排列。其他字母的全排列用递归方法求出
'''
class Solution:
    def permutation(self, S: str) -> List[str]:
        def f(s):
            if len(s)==2:
                return [s, s[::-1]]
            res = []
            for i, ch in enumerate(s):
                l = f(s[:i] + s[i+1:])
                for subs in l:
                    res.append(ch + subs)
            return res

        return f(S)