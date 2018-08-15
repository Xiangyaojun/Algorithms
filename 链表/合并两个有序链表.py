# coding:utf-8
'''
leetcode 21
题目：将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

解析：思路和合并两个有序数组一样
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1

        cur1 = l1
        cur2 = l2
        # 设置新链表的头节点
        if cur1.val <= cur2.val:
            head = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur = cur2
            cur2 = cur2.next
        head.next = None

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur2
                cur2 = cur2.next

        while cur1:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        while cur2:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next
        cur.next = None

        return head


from utils import construct_List_I, travel_List
l1 = construct_List_I([1, 2, 4])
l2 = construct_List_I([1, 3, 4])
solu = Solution()
l3 = solu.mergeTwoLists(l1,l2)
print(travel_List(l3))

