'''
author: 马天骁
date:   2020-5-9
source: leetcode 面试题0408 首个公共祖先 解法一
idea:   求出树的先序遍历及后序遍历，在后序遍历中确定公共祖先所处的可能值，在先序遍历中从后往前找最近的公共祖先
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        post_list = []
        pre_list = []
        def post(t):
            if t == None:
                return
            post(t.left)
            post(t.right)
            post_list.append(t)

        def pre(t):
            if t == None:
                return
            pre_list.append(t)
            pre(t.left)
            pre(t.right)

        pre(root)
        post(root)
        # print(pre_list)
        # print(post_list)
        p_index = post_list.index(p)
        q_index = post_list.index(q)
        max_index = max(p_index, q_index)
        pre_p = pre_list.index(p)
        pre_q = pre_list.index(q)
        i = pre_p if pre_p < pre_q else pre_q
        while pre_list[i] not in post_list[max_index:]:
            i -= 1
        return pre_list[i]
