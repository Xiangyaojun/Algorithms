# coding:utf-8

'''
leetcode 208和783是同一题
给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。

示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树结点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。

解析：
BST的中序遍历就是一个升序数组，而不同节点的最小绝对差就在相邻节点中产生。
1.递归：中序递归遍历，时间：O(n)，空间：O(n)
2.非递归：中序非递归，时间：O(n)，空间：O(n)
'''
import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference_I(self, root):
        # 基于非递归中序遍历
        minDiff = sys.maxsize
        cur = root
        s = []
        result = []
        while cur != None or len(s)>0:
            if cur!=None:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop(-1)
                result.append(cur.val)
                cur = cur.right

        for i in range(1,len(result)):
            temp = result[i]- result[i-1]
            if temp < minDiff:
                minDiff = temp

        return minDiff 

    def getMinimumDifference_II(self,root):
        # 基于递归中序遍历
        minDiff = sys.maxsize
        result = self.inOrder(root,[])

        for i in range(1,len(result)):
            temp = result[i]- result[i-1]
            if temp < minDiff:
                minDiff = temp

        return minDiff

    def inOrder(self,root,result):
        cur = root
        if cur != None:
            self.inOrder(cur.left,result)
            result.append(cur.val)
            self.inOrder(cur.right,result)
        return result