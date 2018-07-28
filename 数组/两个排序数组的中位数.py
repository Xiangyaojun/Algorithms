# coding:utf-8
'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
你可以假设 nums1 和 nums2 均不为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
中位数是 (2 + 3)/2 = 2.5

解析：
1.暴力求解，合并两个有序数组为一整个有序数组，时间复杂度O(n+m),空间复杂度O(1)
2.HashMap求解，时间复杂度O(n),空间复杂度O(n)
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    