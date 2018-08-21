# coding:utf-8

'''
         最优          最坏      平均        空间      稳定
快速排序：O(nlogn)    O(n^2)    O(nlogn)     O(logn)   否

'''


class Solution:
    def quickSort(self, nums, left, right):
        if left < right:
            q = self.partition(nums, left, right)
            self.quickSort(nums, left, q-1)
            self.quickSort(nums, q+1, right)
        return nums

    def partition(self, nums, left, right):
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

solu = Solution()
nums = [5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]
print(solu.quickSort(nums, 0, len(nums)-1))
