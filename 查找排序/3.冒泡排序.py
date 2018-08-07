# coding:utf-8

'''
         最优          最坏      平均        空间      稳定
冒泡排序：O(n)        O(n^2)    O(n^2)       O(1)      是
'''
class Solution:
    def bubbleSort(self, nums):
        flag = False
        for i in range(0, len(nums) - 1):  # n-1趟
            for j in range(len(nums) - 1, i, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    flag = True
            if flag == False:  # 若一次冒泡后，没有交换元素，证明此时已经有序
                return nums
        return nums

solu = Solution()
nums = [5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]
print(solu.bubbleSort([5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]))
