# coding:utf-8

'''
根据前序遍历和中序遍历结果的结果重建二叉树
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self,pre,tin):
        hashmap_inorder = {}
        for i in range(len(tin)):
            hashmap_inorder[tin[i]] = i
        return self.helper(pre, 0, tin, 0, len(tin) - 1, hashmap_inorder)

    def helper(self,pre_nums, pre_start, in_nums,in_start,in_end,hashmap_inorder):
        # 前序遍历数组，前序开始index，中序遍历数组，中序开始index，中序结束index，中序数组的hashmap
        if pre_start>len(pre_nums)-1 or in_start > in_end:
            return
        root = TreeNode(pre_nums[pre_start])
        in_index = hashmap_inorder[pre_nums[pre_start]]
        root.left = self.helper(pre_nums, pre_start+1,in_nums,in_start,in_index-1,hashmap_inorder)
        root.right = self.helper(pre_nums, pre_start+in_index-in_start+1,in_nums,in_index+1,in_end,hashmap_inorder)
        return root

    def preOrder_Recursive(self, root):
        if root!=None:
            print(root.val)  # visit the current node
            self.preOrder_Recursive(root.left)
            self.preOrder_Recursive(root.right)
            

pre_order = [1,2,3,4,5,6,7]
in_order = [3,2,4,1,6,5,7]
solu = Solution()
root = solu.buildTree(pre_order,in_order)
solu.preOrder_Recursive(root)