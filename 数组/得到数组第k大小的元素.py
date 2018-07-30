# coding:utf-8

'''

1.旋转数组中得到最小的元素
解析：
暴力解法：遍历一遍数组就行，算法时间复杂度O(n)
二分查找：在数组两端设置两个指针，不断判断最小元素是否某一边，算法时间复杂度O(logn)

2.旋转数组中得到目标元素
解析：
暴力解法：遍历一遍数组就行，算法时间复杂度O(n)
二分查找：直接从数组中间位置开始寻找，永远在有序的一边判断是否存在目标元素，算法时间复杂度O(logn)

3.任意无序数组中得到第k小的元素

4.两个有序数组的中位数，leetcode 4 Hard
'''

class Solution:
    def minNumberInRotateArray(self,rotateArray):
        #得到旋转数组的最小元素，存在两个有序数组
        left = 0
        right = len(rotateArray)-1
        if rotateArray[left]<rotateArray[right]:
            return rotateArray[0]
        while rotateArray[left]>=rotateArray[right]:
            if right == left + 1:
                return rotateArray[right]
            mid = (left+right)//2
            if rotateArray[left] == rotateArray[mid]:
               return min(rotateArray)
            if rotateArray[left] < rotateArray[mid]:
                #则mid元素位于第一个有序数组中,此时最小元素必然在右半边
                left = mid
            else:
                right = mid
        return rotateArray[right]

solu = Solution()
print(solu.minNumberInRotateArray([5,6,7,8,9,10,10,1,2,3,4]))