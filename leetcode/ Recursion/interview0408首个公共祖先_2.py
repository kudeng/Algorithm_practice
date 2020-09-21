'''
author: 马天骁
date:   2020-5-9
source: leetcode 面试题0408 首个公共祖先 解法一
idea:   如果所求两结点没有祖孙关系，那么其最近公共祖先的特征是，p q结点一定分布于公共祖先的两侧，可以递归求出当前结点
        左右侧是否同时包含p q，来求出公共祖先
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None:
            return root
        if left != None:
            return left
        else:
            return right
