# coding:utf-8

'''
找出单链表第mid个节点并删除
解析：
1.暴力解法：先遍历完链表，得到链表总个数n，再重新遍历到第n/2个元素即为所求，时间复杂度：O(n^2)，空间复杂度：O(1)
2.快慢指针法：定义两个指针都从第一个节点出发，fast指针每次走两步，slow指针每次走一步，这样当fast走完链表时，slow指针刚好走了一半路程，即为所求。
            时间复杂度：O(n)，空间复杂度：O(1)
'''

from utils import construct_List_I, travel_List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findMid(self, head):
        fast = head
        slow = head
        while fast!= None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow

head = construct_List_I([1, 2, 3, 4, 5])
solu = Solution()
print(solu.findMid(head).val)
print(travel_List(head))