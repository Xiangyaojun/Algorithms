# coding:utf-8

'''
阿里面试题：求一个完全二叉树的最后一个节点指针，也就是最后一层的最右节点
解析：
1.暴力求解：层次遍历即可求出最后一个节点，时间复杂度O(n)
2.二分查找法：时间复杂度O(logn) 空间复杂度O(1)
    通过判断右子树是否可以到达树的最深处，如果能到达，则先去右子树，若不能到达，则去左子树
    就这样，递归的划分寻找区间
3.如果二叉树的节点个数是已知的为N，不断除以2，记录奇偶性
  例如知道完全二叉树有9个节点：9 9/2=4 4/2=2 [奇，偶，偶],则反过来从根节点就是左->左->右（偶->偶->奇）
  算法时间复杂度O(logn) 空间复杂度 O(logn)
  完全二叉树的基本性质：编号i的节点的左孩子为2i，右孩子为2i+1，父节点为|_i/2_|
'''

from utils import constructTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getLastNode(self,root):
        cur = root
        # 递归求出完全二叉树的最大深度
        depth = self.getMaxDepth(root)

        level = 1
        while level < depth:
            if (self.getMaxDepth(cur.right) + level)==depth:
                #表明右子树最大深度可以到达二叉树底部，则最后一个节点必然在右子树
                cur = cur.right
            else:
                cur = cur.left
            level += 1
        return cur

    # 得到完全二叉树的最大深度，时间复杂度O(logn)
    def getMaxDepth(self,root):
        cur = root
        count = 0
        if cur==None:
            return 0
        while cur!=None:
            count+=1
            cur=cur.left
        return count

    def getLastNode_1(self,root,N):
        '''
        若知道完全二叉树有多少个节点，则可以利用完全二叉树的基本性质：编号i的节点的左孩子为2i，右孩子为2i+1，父节点为|_i/2_|
        如果二叉树的节点个数是已知的为N，不断除以2，记录奇偶性
        例如知道完全二叉树有9个节点：9 9/2=4 4/2=2 [奇，偶，偶],则反过来从根节点就是左->左->右（偶->偶->奇）
        算法时间复杂度O(logn)
        '''
        if N <= 1:
            return root
        cur = root
        s = [N]
        while N/2 > 1:
            s.append(N/2)
            N /= 2
        i = len(s)-1
        while i >= 0:
            if s[i] % 2 == 0:
                cur = cur.left
            else:
                cur = cur.right
            i -= 1
        return cur

solu = Solution()
root = constructTree()
print(solu.getLastNode(root).val)
