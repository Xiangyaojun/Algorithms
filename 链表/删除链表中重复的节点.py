# -*- coding:utf-8 -*-

'''
题目:在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
'''
from utils import construct_List_I, travel_List
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, root):
        '''
        第一个重复点保留，后面的重复点都删除
        输入: 1->2->3->3->4->4->5
        输出: 1->2->5
        '''
        pre = None
        cur = root
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                if pre:  # 如果第一个节点就是重复节点，此时pre==None
                    pre.next = cur.next
                else:
                    root = cur.next
            else:
                pre = cur
            cur = cur.next
        return root

    def deleteDuplicates(self, head):
        '''
        第一个重复点保留，后面的重复点都删除
        输入: 1->1->2->3->3
        输出: 1->2->3
        '''
        pre = None
        cur = head
        while cur:
            if pre and pre.val == cur.val:
                while pre and cur:
                    if pre.val == cur.val:
                        cur = cur.next
                    else:
                        break
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return head
slou = Solution()
root = construct_List_I([2,2,4,4,4])
root = slou.deleteDuplicates(root)
print(travel_List(root))