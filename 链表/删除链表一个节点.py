# coding:utf-8

'''
删除链表的某个节点，不知道头结点
注意：该节点不是头结点，也不是尾节点。
解析：
要删除一个节点需要知道该节点的前驱节点指针，但这是一个不知道头结点的链表，无法得到前驱，只能交换value来做到删除。
'''

from utils import construct_List_I, travel_List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNode(self, cur):
        cur.val = cur.next.val
        cur.next = cur.next.next

head = construct_List_I()
solu = Solution()
node = head.next.next.next
solu.removeNode(node)
print(travel_List(head))