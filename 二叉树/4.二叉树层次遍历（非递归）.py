# coding:utf-8

'''
leetcode 102. 二叉树的层次遍历
题目：给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

leetcode 107. 二叉树的层次遍历 II
题目：
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
解析：需要设置rear指针表示最近入队节点，当出队访问到每一层的最右节点时,最近入队的节点就是下一层的最右节点
'''

from utils import constructTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = []
        rear = root  # 指向最近入队节点
        last = root  # 指向最右节点
        queue.append(root)

        row = []
        while len(queue) > 0:
            cur = queue.pop(0)
            row.append(cur.val)
            if cur.left:
                queue.append(cur.left)
                rear = cur.left
            if cur.right:
                queue.append(cur.right)
                rear = cur.right
            if cur == last:  # 如果当前出队节点指向最右节点，证明这一层已经访问完
                result.append(row)
                row = []
                last = rear
        return result

solu = Solution()
root = constructTree()
print(solu.levelOrder(root))
