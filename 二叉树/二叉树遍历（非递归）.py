# coding:utf-8

'''
二叉树三种不同顺序遍历的非递归算法
另外可以看看博客：https://blog.csdn.net/qiaoruozhuo/article/details/40586443

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def preOrder_Recursive(self, root):
        """
        :type root:TreeNode
        """
        if root!=None:
            print(root.val) #visit the current node
            self.preOrder_Recursive(root.left)
            self.preOrder_Recursive(root.right)
            
    def preOrder(self, root):
        """
        :type root:TreeNode
        """
        s = []
        cur = root
        while cur!=None or len(s)>0:
            if cur!=None:
                print(cur.val)
                s.append(cur)
                cur = cur.left
            else:#此时，必然是访问到最左节点后，当前节点为空，只能出栈
                cur = s.pop(-1)
                cur = cur.right


    def inOrder(self, root):
        """
        :type root:TreeNode
        """
        s = []
        cur = root
        while cur!=None or len(s)>0:
            if cur!=None:
                s.append(cur)
                cur = cur.left
            else:#此时，必然是访问到最左节点后，当前节点为空，只能出栈
                cur = s.pop(-1)
                print(cur.val)
                cur = cur.right

    def postOrder(self, root):
        """
        :type T:TreeNode
        """
        s = []
        cur = root
        rear = None #设置一个指针，表示当前节点是否被访问过
        while cur!=None or len(s)>0:
            if cur!=None:
                s.append(cur)
                cur = cur.left
            else:
                temp = s[-1] #此时不需要立即出栈，因为后序遍历需要访问右子树后，才访问当前父节点
                if temp.right!=None and rear!=temp.right:
                    cur = temp.right
                else:
                    '''
                    存在两种情况：
                    1.此时当前节点的右子树为空，则当前节点为叶子节点，应立即访问 
                    2.此时当前节点的右子树已被访问，则希望置空cur，以此访问父节点。此时左右子树都已经访问完毕
                    '''
                    cur = s.pop(-1)
                    print(cur.val)
                    rear = cur
                    cur = None # 注意：还需要cur置空操作

    def constructTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        return root

solu = Solution()
root = solu.constructTree()
solu.postOrder(root)