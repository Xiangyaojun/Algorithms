# coding:utf-8

'''
leetcode 35
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
解析：
1.暴力解法:直接一个一个遍历整个数组查找，时间复杂度O(n+m)
2.二分查找法:时间复杂度O(logn)

'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while True:
            mid = (begin + end)//2
            if nums[mid]==target:
                return mid
            elif target > nums[mid]:
                if mid==len(nums) -1 or target < nums[mid+1]:
                    return mid +1
                else:
                    begin = mid +1
            elif target < nums[mid]:
                if mid==0 or target > nums[mid-1]:
                    return mid
                else:
                    end = mid - 1