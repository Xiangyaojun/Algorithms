# coding:utf-8

'''
leetcode 237
题目：给定一个节点的指针，要求删除该节点，不知道头结点
注意：该节点不是头结点，也不是尾节点。
解析：
要删除一个节点需要知道该节点的前驱节点指针，但这是一个不知道头结点的链表，无法得到前驱，只能交换value来做到删除。

leetcode 203
题目：给定节点头指针，删除链表中的所有val为某个值的节点
解析：从头指针开始遍历，同时设置一个指针记录前驱指针，这样依次删除。
'''

from utils import construct_List_I, travel_List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, cur):
        # 题目237
        cur.val = cur.next.val
        cur.next = cur.next.next

    def removeElements(self,root,val):
        # 题目203
        cur = root
        pre = None
        while cur!=None:
            if cur.val==val:
                if pre==None:
                    root = cur.next
                    cur = cur.next
                else:
                    pre.next = cur.next
                    cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return root





head = construct_List_I([1,2,1,4,1])
solu = Solution()

head = solu.removeElements(head,1)
print(travel_List(head))