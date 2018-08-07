'''
可以参考博客：https://blog.csdn.net/qiaoruozhuo/article/details/40586443
解析：
1.前序遍历（中左右）的过程可以看成压入一个节点就马上访问该节点的过程
2.中序遍历（左中右）的过程需要不断压栈到最左，在递归pop节点访问
3.后序遍历（左右中）的过程常规需要多设置一个指针标志父节点是否被访问过，另外一个角度也可以将前序遍历的过程改成（中右左），在倒序就是结果
'''

from utils import constructTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def postOrder_I(self, root):
        result = []
        s = []
        cur = root
        rear = None  # 设置一个指针，表示当前节点是否被访问过
        while cur!=None or len(s)>0:
            if cur!=None:
                s.append(cur)
                cur = cur.left
            else:
                temp = s[-1] # 此时不需要立即出栈，因为后序遍历需要访问右子树后，才访问当前父节点
                if temp.right!=None and rear!=temp.right:
                    cur = temp.right
                else:
                    '''
                    存在两种情况：
                    1.此时当前节点的右子树为空，则当前节点为叶子节点，应立即访问 
                    2.此时当前节点的右子树已被访问，则希望置空cur，以此访问父节点。此时左右子树都已经访问完毕
                    '''
                    cur = s.pop(-1)
                    result.append(cur.val)
                    rear = cur
                    cur = None # 注意：还需要cur置空操作

        return result

    def postOrder_II(self,root):  # 前序
        # 基于前面前序的思想，前序是中左右 -> 中右左 -> 倒序最后的结果数组，就可以得到 左右中的后序遍历结果
        result = []
        s = []
        cur = root
        s.append(cur)
        while len(s) > 0:
            cur = s.pop(-1)
            if cur != None:
                result.append(cur.val)
                s.append(cur.left)
                s.append(cur.right)

        return result[::-1]  # 倒序最后的结果

solu = Solution()
root = constructTree()
print(solu.postOrder_I(root))
print(solu.postOrder_II(root))