# coding:utf-8

'''

'''

from utils import constructTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def preOrder_I(self, root):
        s = []
        result = []
        cur = root
        while cur!=None or len(s) > 0:
            if cur!=None:
                result.append(cur.val)
                s.append(cur)
                cur = cur.left
            else:#此时，必然是访问到最左节点后，当前节点为空，只能出栈
                cur = s.pop(-1)
                cur = cur.right
        return result

solu = Solution()
root = constructTree()
print(solu.preOrder_I(root))
