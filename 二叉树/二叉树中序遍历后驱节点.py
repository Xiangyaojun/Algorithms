# coding:utf-8

'''
题目：二叉树的下一个节点

题目描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
解析：要找到二叉树某个节点中序遍历的后驱节点，需要分情况讨论

1.如果给定节点存在右子树，则后驱节点为右子树的最左节点
2.如果给定节点没有右子树，且给定节点是其父节点的左孩子，此时后驱节点为给定节点的父节点
3.如果给定节点没有右子树，且给定节点是其父节点的右孩子，则表明此时中序遍历已经遍历完以给定节点的父节点为根节点的子树，此时后驱节点要么为给定节点的祖父节点，要么就不存在。
'''
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def GetNext(self, node):
        if node and node.right:  # 如果节点存在右子树，则后驱节点为右子树的最左节点
            node = node.right
            while node.left:
                node = node.left
            return node
        elif node.next and node.next.left == node:  # 如果节点没有右子树，并且它还是父节点的左孩子
            return node.next
        elif node.next and node.next.right == node:  # 如果节点没有右子树，并且它还是父节点的右孩子
            if node.next.next and node.next.next.left == node.next:  # 如果父节点为根节点的子树在祖父节点的左边
                return node.next.next
        else:
            return None