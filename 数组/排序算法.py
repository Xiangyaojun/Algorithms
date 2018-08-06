# coding:utf-8

'''
所有常见排序算法的实现
         最优          最坏      平均      空间   稳定
冒泡排序：O(n)        O(n^2)    O(n^2)     O(n)    是
快速排序：O(nlogn)    O(n^2)    O(nlogn)   O(n)    否
'''
class Solution:
    def bubbleSort(self, nums):
        flag = False
        for i in range(0,len(nums)-1):
            for j in range(len(nums)-1,i,-1):
                if nums[j]<nums[j-1]:
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
                    flag = True
            if flag == False:#若一次冒泡后，没有交换元素，证明此时已经有序
                return nums
        return nums

    def quickSort(self, nums, left, right):
        if left < right:
            q = self.partition(nums, left, right)
            self.quickSort(nums, left, q-1)
            self.quickSort(nums, q+1, right)
        return nums

    def partition(self, nums, left, right):
        pivot = nums[left] 
        while left < right:
            while left < right and nums[right] >= pivot: right -= 1
            nums[left] = nums[right] 
            while left < right and nums[left] <= pivot: left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left
        
solu = Solution()
nums = [5,3,2,5,1,5,7,3,9,8,7]
print(solu.quickSort(nums,0,len(nums)-1))
