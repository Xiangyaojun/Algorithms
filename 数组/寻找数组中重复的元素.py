# coding:utf-8

'''
剑指offer 3
题目：找出数组中重复的元素，
在一个长度为n的数组里所有数字都在0~n-1的范围内。数组中某些数字是重复的。
解析：
1.暴力求解：先将数组排好序，再寻找，时间复杂度O(nlogn),空间复杂度O(1)
2.HashMap求解：遍历一遍数组，建立hash表记录次数，时间复杂度O(n),空间复杂度O(n)
3.最优解：基于数组中元素都在0~n-1范围内这一特点，
'''
class Solution:
    def findDuplicate(self, nums):
        result = []
        i = 0 #设置一个指针，遍历数组
        while i<len(nums):
            if nums[i] != i and nums[nums[i]] != nums[i]: # 若当前位置下标不等，以及数值位置下标同样不等
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
                continue
            elif nums[i] != i and nums[nums[i]] == nums[i]:
                result.append(nums[i])
            i += 1
        return result

solu = Solution()
nums = [2,1,3,4,5,3,3,4,5]
print(solu.findDuplicate(nums))

