# coding:utf-8
'''
leetcode 1
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
示例：
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
解析：
1.暴力求解，时间复杂度O(n^2),空间复杂度O(1)
2.HashMap求解，时间复杂度O(n),空间复杂度O(n)
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        result = []
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in hashmap:
                result.append(hashmap[temp])
                result.append(i)
                return result
            hashmap[nums[i]] = i
        return result

