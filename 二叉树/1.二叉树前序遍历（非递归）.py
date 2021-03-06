# coding:utf-8

'''
可以参考博客：https://blog.csdn.net/qiaoruozhuo/article/details/40586443
解析：
前序遍历（中左右）的过程可以看成压入一个节点就马上访问该节点的过程
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
        result = []
        s = []
        cur = root
        while cur!=None or len(s) > 0:
            if cur!=None:
                result.append(cur.val)
                s.append(cur)
                cur = cur.left
            else:  # 此时，必然是访问到最左节点后，当前节点为空，只能出栈
                cur = s.pop(-1)
                cur = cur.right
        return result

    def preOrder_II(self,root):  # 前序
        # 思想很简单，前序遍历是一个中左右的顺序，刚好符合栈的一个入栈出栈的顺序
        result = []
        s = []
        s.append(root)
        while len(s) != 0:
            node = s.pop()
            if node == None:
                continue
            result.append(node.val)
            s.append(node.right)
            s.append(node.left)
        return result

solu = Solution()
root = constructTree()
print(solu.preOrder_I(root))
print(solu.preOrder_II(root))