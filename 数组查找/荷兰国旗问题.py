# coding:utf-8

'''
一、题目
    现有红、白、蓝三个不同颜色的小球，乱序排序在一起，
    请重新排列这些小球，使得红白蓝三色的同颜色的球在一起。
二、问题转换：
    给定数组array[0,...n-1],元素只能取0,1,2三个值，设计算法，
    使得数组排列成“0000...00001111....11112222...2222”
三、解题思路：
    * 借鉴快速排序中partition的过程
    * 初始化： left = 0，k = 0，right = N
    * 打算[0,left]全是0, (left,k)全是1,
      [k,right)是未遍历的区域, [right,len(nums))全是2
四、解题步骤：
    划分三个区域
    0：[0,left]
    1:[left+1,right-1] 设置K移动
    2:[right,len(nums)-1]
'''
class Solution:
    def sortColors(self,nums):
        #未访问区域为[k,right)
        left = -1
        right = len(nums)
        k = 0
        while k > left and k < right:
            if nums[k] == 0:
                left = left + 1
                self.swap(nums, left, k)
            elif nums[k] == 1:
                k += 1
            elif nums[k] == 2:
                right = right - 1
                self.swap(nums, right, k)
        return nums

    def swap(self,nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

solu = Solution()
nums = [2, 1, 2, 2, 0, 1, 2, 2, 1]
print(solu.sortColors(nums))