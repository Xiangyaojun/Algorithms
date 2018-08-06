'''
一、题目
    现有红、白、蓝三个不同颜色的小球，乱序排序在一起，
    请重新排列这些小球，使得红白蓝三色的同颜色的球在一起。
二、问题转换：
    给定数组array[0,...n-1],元素只能取0,1,2三个值，设计算法，
    使得数组排列成“0000...00001111....11112222...2222”
三、解题思路：
    * 借鉴快速排序中partition的过程
    * 初始化： begin = 0，cur = 0，end = N-1
    * 打算[0,begin)全是0, [begin,cur)全是1,
      [cur,end)是未遍历的数, [end,size-1)全是2
四、解题步骤：
    
'''
class Solution:
    def sortColors(self,nums):
        left=0
        right=len(nums)
        for k in range(0, right):#保证[left,right-1]区域为0
            if nums[k] == 0:
                temp = nums[left]
                nums[left] = nums[k]
                nums[k] = temp
                left += 1
            elif nums[k] == 2:
                right -= 1
                temp = nums[right]
                nums[right] = nums[k]
                nums[k] = temp
                k -= 1
        return nums
solu = Solution()
nums = [2,1,2,2,0,0,1,2,0,2,1]
print(solu.sortColors(nums))