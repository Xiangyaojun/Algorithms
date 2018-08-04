# coding:utf-8

'''
剑指offer 6
题目：倒序遍历链表，从尾到头打印
1.如果允许改变链表结构，可以考虑先反转链表，再从头到尾遍历，时间：O(n)，空间：O(1)
2.如果不允许改变链表结构，可以用栈来存储链表数据，或者采用递归的方式,时间：O(n)，空间：O(n)
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def construct_List(self,nums):
        #尾插法构建链表
        if len(nums)==0:
            return None
        root = ListNode(nums[0])
        cur = root
        for i in range(1, len(nums)):
            node = ListNode(nums[i])
            cur.next = node
            cur = node
        return root

    def construct_List_1(self,nums):
        #头插法构建链表
        if len(nums)==0:
            return None
        root = ListNode(nums[0])
        for i in range(1, len(nums)):
            node = ListNode(nums[i])
            node.next = root
            root = node
        return root

    def travel_List(self, root):
        cur = root
        result = []
        while cur!=None:
            result.append(cur.val)
            cur = cur.next
        return result

    def reverse_travel(self, root):
        cur = root
        if cur != None:
            self.reverse_travel(cur.next)
            print(cur.val)
        else:
            return


solu = Solution()
root = solu.construct_List([1, 2, 3, 4, 5])
solu.reverse_travel(root)
