# coding:utf-8

'''
leetcode 206：反转链表 I
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL


leetcode 92：反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

'''
from utils import construct_List_I, travel_List

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reverseList_I(self, root):
        if root == None: return root
        cur = root.next
        root.next = None

        while cur != None:
            next = cur.next
            cur.next = root
            root = cur
            cur = next

        return root

    def reverseList_II(self, root, m, n):
        # 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转
        if root == None or n <= m:
            return root
        i = 1
        cur = root
        pre_head = None
        while i < m:
            if cur == None:
                return root
            pre_head = cur
            cur = cur.next
            i += 1

        # pre_head为第m-1个节点，cur为第m个节点,此时i=m
        reverse_start = cur
        reverse_end = cur
        cur = cur.next

        while i < n:
            next = cur.next
            cur.next = reverse_start
            reverse_start = cur
            cur = next
            i += 1
        reverse_end.next = cur
        if pre_head == None:
            return reverse_start
        else:
            pre_head.next = reverse_start
            return root

root = construct_List_I([1, 2, 3, 4, 5, 6])
solu = Solution()
root = solu.reverseList_II(root, 1, 6)
print(solu.travelList(root))
