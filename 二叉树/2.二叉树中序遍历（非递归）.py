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

    def inOrder(self, root):
        s = []
        result = []
        cur = root
        while cur!=None or len(s)>0:
            if cur!=None:
                s.append(cur)
                cur = cur.left
            else:
                # 此时，必然是访问到最左节点后，当前节点为空，只能出栈
                cur = s.pop(-1)
                result.append(cur.val)
                cur = cur.right
        return result

solu = Solution()
root = constructTree()
print(solu.inOrder(root))
