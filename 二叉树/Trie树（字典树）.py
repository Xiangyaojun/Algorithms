# coding:utf-8

'''
Tire树（字典树）的查询与构建
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.data = ""
        self.next = {}

class TrieTree:
    def __init__(self):
        self.root = TreeNode()
    def buildTree(self, str_arrays):


    def insert(self, key, value = None):
        

            

pre_order = [1,2,3,4,5,6,7]
in_order = [3,2,4,1,6,5,7]
solu = Solution()
root = solu.buildTree(pre_order,in_order)
solu.preOrder_Recursive(root)