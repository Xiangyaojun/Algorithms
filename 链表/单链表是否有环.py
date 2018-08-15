# coding:utf-8

'''
leetcode 141 142
给定一个链表，判断链表中是否有环。
如果由环，则返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
注意：不允许修改给定的链表

解析：
1.建立一个hash表，判断后面访问的节点是否出现过
2.快慢指针法：设置一个快指针每次走2步，慢指针每次走1步，两个指针同时出发，当两个指针交汇时，则链表有环。
找出环的开始点：记录第一次相遇的点，分别设置两个指针，一个是头节点，一个从相遇节点开始走，都每次走一个，当两个指针相遇的点就是起始点。
'''
from utils import construct_List_I

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, root):
        if root == None: return None
        slow = root
        fast = root
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == slow and fast.next!=None:
            pos = fast
            cur = root
            while pos!=cur:
                pos = pos.next
                cur = cur.next
            return pos
        else:
            return None
root = construct_List_I([1,2,3,4,5])
solu = Solution()
print(solu.detectCycle(root))
