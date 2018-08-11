# coding:utf-8

'''
剑指offer 6
题目：倒序遍历链表，从尾到头打印
1.如果允许改变链表结构，可以考虑先反转链表，再从头到尾遍历，时间：O(n)，空间：O(1)
2.如果不允许改变链表结构，可以用栈来存储链表数据，或者采用递归的方式,时间：O(n)，空间：O(n)
'''
from utils import construct_List_I, travel_List

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reverse_travel(self, root):
        cur = root
        if cur != None:
            self.reverse_travel(cur.next)
            print(cur.val)
        else:
            return

root = construct_List_I([1, 2, 3, 4, 5])
solu = Solution()
solu.reverse_travel(root)
