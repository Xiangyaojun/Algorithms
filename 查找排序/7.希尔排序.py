# coding:utf-8

'''
实质上是分组插入排序，也叫缩小增量排序
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
1.插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
2.但直接插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位
         最优          最坏      平均        空间      稳定
希尔排序： O(n)      O(n^2)    O(n^2)       O(1)      否
'''


class Solution:
    def shellSort(self,nums):
        step = len(nums) // 2
        while step > 0:
            for i in range(step, len(nums)):
                # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
                while i >= step and nums[i - step] > nums[i]:
                    nums[i], nums[i - step] = nums[i - step], nums[i]
                    i -= step
            step = step // 2
        return nums

solu = Solution()
print(solu.shellSort([5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]))
