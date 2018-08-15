# coding:utf-8

'''
            最优        最坏      平均        空间      稳定
折半插入排序：O(n)      O(n^2)    O(n^2)       O(1)      是
'''


class Solution:
    def insertSort(self, nums):
        for i in range(1, len(nums)):  # n-1趟
            if nums[i] < nums[i - 1]:
                temp = nums[i]
                low = 0
                high = i-1
                while low < high:
                    mid = (low+high)//2
                    if temp > nums[mid]:
                        low = low + 1
                    else:
                        high = high - 1
                # 插入位置为high位置
                for j in range(i-1, high-1,-1):  # [high, i-1]位置的元素依次后移
                    nums[j+1] = nums[j]
                nums[high] = temp
        return nums


solu = Solution()
print(solu.insertSort([3, 5, 2, 5, 1, 5, 7, 3, 9, 8, 7]))
