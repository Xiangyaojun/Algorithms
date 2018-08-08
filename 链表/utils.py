# coding:utf-8

'''
尾插法和头插法构建单链表
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def construct_List_I(nums):
    # 尾插法构建链表:正序
    if len(nums) == 0:
        return None
    root = ListNode(nums[0])
    cur = root
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        cur.next = node
        cur = node
    return root


def construct_List_II(nums):
    # 头插法构建链表：倒序
    if len(nums) == 0:
        return None
    root = ListNode(nums[0])
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        node.next = root
        root = node
    return root


def travel_List(root):
    # 遍历链表
    cur = root
    result = []
    while cur != None:
        result.append(cur.val)
        cur = cur.next
    return result
