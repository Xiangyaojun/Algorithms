#coding:utf-8

'''
leetcode 222
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入: 
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6
解析：
1.暴力求解：遍历一遍所有节点，时间复杂度O(n)
2.二分查找法：基于任意节点的左右子树，必然有一个是完全二叉树，算法时间复杂度O(logn)
'''
from utils import constructTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self,root):
        import math
        cur = root
        if cur == None:
            return 0
        #得到左右子树的最大深度，看看哪个子树是完全二叉树
        left_depth = self.getMaxDepth(cur.left)
        right_depth = self.getMaxDepth(cur.right)
        if left_depth == right_depth:
            # 若两个子树深度相等，可以确定左子树是完全二叉树，直接计算出左子树的节点个数
            return int(math.pow(2,left_depth) - 1) + self.countNodes(cur.right) + 1
        elif left_depth > right_depth:
            # 若左子树深度大于有子树，可以确定右子树是完全二叉树，直接计算出右子树的节点个数
            return self.countNodes(cur.left) + int(math.pow(2, right_depth) - 1) + 1

    def getMaxDepth(self,root):
        cur = root
        depth = 0
        while cur!=None:
            depth += 1
            cur = cur.left
        return depth

solu = Solution()
root = constructTree()
print(solu.countNodes(root))
