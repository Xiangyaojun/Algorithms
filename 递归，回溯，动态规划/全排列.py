# coding:utf-8
'''
leetcode 46
全排列（没有重复元素的序列）
递归算法:缺点就是最后还需要去重
解析：
直观来看，存在n!个不同的排列，时间复杂度为O(n*n!)

leetcode 47
全排列（有重复元素的序列）
1.递归算法 :
2.非递归算法

'''
class Solution:

    def permutation(self, nums, begin, end):
        # 递归算法:当数组中有重复元素时，会重复输出排列，需要在加一步去重的工作
        # 假设总共有n个元素，其核心是：将每个元素放到余下n-1个元素组成的队列最前方，然后对剩余元素进行全排列，依次递归下去
        if begin == end:
            print(nums)
        else:
            for i in range(begin, end+1):
                nums[begin], nums[i] = nums[i], nums[begin]
                self.permutation(nums, begin+1, end)
                nums[begin], nums[i] = nums[i], nums[begin]

    def permute(self,nums):

        pass

solu = Solution()
nums = [1, 2, 3, 4]
solu.permutation(nums, 0, len(nums)-1)
