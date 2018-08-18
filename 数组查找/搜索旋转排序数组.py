'''
leetcode 33. 搜索旋转排序数组
题目：
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
注意：假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
1.暴力解法：直接遍历搜索，复杂度O(n)
2.二分查找法：基于原始的二分查找，取mid点，可以将原始数组分为两部分，[0,mid-1]和[mid+1,size-1]，若nums[mid]不是目标值，则必然在左右两部分其中一个，
而这两部分其中一个必然是有序的，可以之间判断target是否在范围内。
'''


class Solution:
    def binarySearch(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

solu = Solution()
print(solu.binarySearch([3,1], 0))
