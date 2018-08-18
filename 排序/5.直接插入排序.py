# coding:utf-8

'''
            最优        最坏      平均         空间      稳定
直接插入排序：O(n)      O(n^2)    O(n^2)       O(1)       是
'''


class Solution:
    def insertSort(self, nums):
        for i in range(1, len(nums)):  # n-1趟
            if nums[i] < nums[i-1]:
                temp = nums[i]
                j = i-1
                while j >= 0 and nums[j] > temp:
                    nums[j+1] = nums[j]
                    j = j-1
                nums[j+1] = temp
        return nums

solu = Solution()
print(solu.insertSort([3, 5, 2, 5, 1, 5, 7, 3, 9, 8, 7]))
