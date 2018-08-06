# coding:utf-8

'''
leetcode 189
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
解析:
1.暴力求解：一个一个元素旋转，时间复杂度O(n) 需要移动k*n次，速度较慢
2.反转数组法：利用k可以将原始数组分为两个部分，每部分各自反转一次，在最后整个数组一起反转一次
'''
class Solution:
    def rotate(self,nums,k):
        k = k%len(nums)
        if k <= 0: return
        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
        
    def reverse(self, nums, begin, end):
        while begin < end:
            temp = nums[begin]
            nums[begin] = nums[end]
            nums[end] = temp
            begin += 1
            end -= 1
        return nums

solu = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
solu.rotate(nums,11)
print(nums)