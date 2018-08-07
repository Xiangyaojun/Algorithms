# coding:utf-8

'''
         最优          最坏      平均        空间      稳定
选择排序：O(n^2)      O(n^2)    O(n^2)       O(1)      否
'''


class Solution:
    def selectSort(self,nums):
        for i in range(len(nums)-1):  # n-1趟
            min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            nums[min], nums[i] = nums[i],nums[min]
        return nums

solu = Solution()
nums = [5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]
print(solu.selectSort([5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]))
