from utils import constructTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def preOrder_Recursive(self, root):
        if root!=None:
            print(root.val) #visit the current node
            self.preOrder_Recursive(root.left)
            self.preOrder_Recursive(root.right)

solu = Solution()
root = constructTree()
solu.preOrder_Recursive(root)