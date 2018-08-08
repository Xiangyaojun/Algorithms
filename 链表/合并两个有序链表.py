# coding:utf-8
'''
leetcode 21
合并两个有序链表
解析：思路和合并两个有序数组一样
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        cur1 = l1
        cur2 = l2
        head = None
        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
               cur1 = cur1.next
