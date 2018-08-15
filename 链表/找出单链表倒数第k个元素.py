# coding:utf-8

'''
找出单链表倒数第k个节点
注意：输入k一定合法
类似题：leetcode 19 删除链表的倒数第K个节点（只不过要记住一点：若要在单链表中删除一个节点，需要得到该节点的前驱）
解析：
1.暴力解法：先遍历完链表，得到链表总个数n，再重新遍历到第n-k个元素即为所求，时间复杂度：O(n^2)，空间复杂度：O(1)
2.快慢指针法：定义两个指针都从第一个节点出发，第一个指针走k步后，第二个指针再出发，这样两个指针的间隔为k，一旦第一个指针到达尾部，第二个指针即为所求节点
            时间复杂度：O(n)，空间复杂度：O(1)
'''

from utils import construct_List_I, travel_List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findKthFromEnd(self, head, k):
        fast = head
        slow = head

        i = k
        while fast and i > 0:
            fast = fast.next
            i = i - 1
        if i > 0: return None
        while slow and fast:
            slow = slow.next
            fast = fast.next
        return slow

    def removeKthFromEnd(self, head, k):
        fast = head
        slow = head
        pre = None

        i = k
        while i > 0:
            fast = fast.next
            i = i-1
        if fast==None:
            head = slow.next
            return head

        while fast!=None:
            pre = slow
            slow = slow.next
            fast = fast.next

        pre.next = slow.next
        slow.next = None
        return head

head = construct_List_I([1, 2, 3, 4, 5])
solu = Solution()
print(solu.findKthFromEnd(head, 5).val)
print(travel_List(head))