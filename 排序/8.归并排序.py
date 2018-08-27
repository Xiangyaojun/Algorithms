# coding:utf-8

'''
           最优          最坏          平均        空间      稳定
归并排序：O(nlogn)      O(nlogn)    O(nlogn)       O(n)      否
'''


class Solution:
    def merge(self,a,b):
        c = []
        i = 0
        j = 0
        while i<len(a) and j<len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        while i < len(a):
            c.append(a[i])
            i += 1
        while j<len(b):
            c.append(b[j])
            j += 1
        return c

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left,right)

solu = Solution()
print(solu.mergeSort([5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]))
